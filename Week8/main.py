from fastapi import FastAPI, Request, Response, Form, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

import mysql.connector, os, re

load_dotenv()

#define class for request body of PATCH username feature (Week7)
class NewUsername(BaseModel):
    name: str

#database parameters [Week7: changed to environment variables]
db_host=os.getenv("db_host")
db_user=os.getenv("db_user")
db_pw=os.getenv("db_pw")
db_database=os.getenv("db_database")

print("============================")

db_config = {
    "host": db_host,
    "database": db_database,
    "user": db_user,
    "password": db_pw
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 3,
                                                      host = db_host,
                                                      database = db_database,
                                                      user = db_user,
                                                      password = db_pw)

print(cnxpool.pool_name, cnxpool.pool_size)

print("============================")

#sessionMiddleWare secret key parameter [Week7: changed to environment variables]
session_secret_key=os.getenv("session_secret_key")

#Templates - FastAPI https://fastapi.tiangolo.com/advanced/templates/ & https://fastapi.tiangolo.com/reference/templating/
templates = Jinja2Templates(directory="templates")

def update_request_session(session):
    website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)
    website_db_cursor = website_db.cursor()

    cmd = "SELECT id, username, password, name FROM member WHERE username = %s"
    website_db_cursor.execute(cmd,(session["username"],))
    website_db_result = website_db_cursor.fetchone()
    session["member_id"] = website_db_result[0]
    session["username"] = website_db_result[1]
    session["name"] = website_db_result[3]

#creates a webapp
app = FastAPI()

#Don't forget SessionMiddleware...忘了這個於是debug了許久orz
app.add_middleware(SessionMiddleware, secret_key=session_secret_key, max_age=None)

#Week8: Trying CORS
#app.add_middleware(CORSMiddleware, allow_origins=['http://127.0.0.1:8052'], allow_methods=['GET'])

#mount the static files. without this css and js don't work
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
# main page renders login.html template.
async def index(request: Request):
    #if all(item in request.session for item in ("member_id", "username", "name")):
    #    print(request.session["member_id"],request.session["username"],request.session["name"])
    #else:
    #    print("nothing inside request.session")
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/member")
# member page first checks if session has signin record. if no, redirects to login. if yes, renders loginsuccess.html template.
async def member(request: Request):
    if "member_id" not in request.session or request.session["member_id"] == None:
        return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)  
    else:
        #update user display name
        update_request_session(request.session)
        
        # website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)
        # website_db_cursor = website_db.cursor()

        connection_object = cnxpool.get_connection()
        print(connection_object)
        website_db_cursor = connection_object.cursor()
        
        #member id & message id for task 6
        cmd = "SELECT member.name, message.content, member.id, message.id FROM message JOIN member ON message.member_id = member.id"
        website_db_cursor.execute(cmd)
        website_db_result = website_db_cursor.fetchall()
        print("connection pool method success!")

        return templates.TemplateResponse("loginsuccess.html", {"request": request,
                                                                "member_id": request.session["member_id"],
                                                                "member_name": request.session["name"],
                                                                "messages": website_db_result})

@app.get("/error")
#error page borrowed from week4
async def error(request: Request, message: str | None = None):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.post("/signup")
#new member sign-up logic
async def signup(request: Request, signup_name_text: str | None = Form(None), signup_username_text: str | None = Form(None), signup_password_text: str | None = Form(None)):
    #front-end also has verifying logic, see static/script.js
    if signup_name_text == None or signup_username_text == None or signup_password_text == None:
        return RedirectResponse("/error?message=One or more required fields is/are blank!", status_code=status.HTTP_303_SEE_OTHER)
    elif not re.match("^(?=.*[@#$%])[A-Za-z0-9@#$%]{4,8}$",signup_password_text):
        print("Regex match failed")
        return RedirectResponse("/error?message=Regex match failed", status_code=status.HTTP_303_SEE_OTHER)
    else:
        print("Regex match passed!")

    website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)
    website_db_cursor = website_db.cursor()

    cmd = "SELECT username FROM member WHERE username = %s"
    website_db_cursor.execute(cmd, (signup_username_text,))
    website_db_result = website_db_cursor.fetchone()
    if website_db_result != None:
        #print(website_db_result)
        return RedirectResponse("/error?message=此帳號已被使用 Repeated username", status_code=status.HTTP_303_SEE_OTHER)

    else:
        #print("Did not find somebody with same username")
        cmd = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        website_db_cursor.execute(cmd, (signup_name_text, signup_username_text, signup_password_text))
        website_db.commit()
        #print("Added member:", signup_username_text)
        return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
    
@app.post("/signin")
#existing member sign-in logic
async def signin(request: Request, signin_username_text: str | None = Form(None), signin_password_text: str | None = Form(None)):
    #front-end also has verifying logic, see static/script.js
    if signin_username_text == None or signin_password_text == None:
        return RedirectResponse("/error?message=One or more required fields is/are blank!", status_code=status.HTTP_303_SEE_OTHER)
    
    website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)
    website_db_cursor = website_db.cursor()

    cmd = "SELECT id, username, password, name FROM member WHERE username = %s"
    website_db_cursor.execute(cmd,(signin_username_text,))
    website_db_result = website_db_cursor.fetchone()
    if website_db_result == None:
        return RedirectResponse("/error?message=User not found!", status_code=status.HTTP_303_SEE_OTHER)
    elif signin_password_text == website_db_result[2]:
        request.session["member_id"] = website_db_result[0]
        request.session["username"] = website_db_result[1]
        request.session["name"] = website_db_result[3]
        #print("User", request.session["username"], "signed in.")
        return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)

    else:
        return RedirectResponse("/error?message=Incorrect password.", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/signout")
#signed-in member signout logic (or force clear session by directly typing url)
async def signout(request: Request):
    if "member_id" in request.session:
        #print("User", request.session["username"], "signing out.")
        del request.session["member_id"], request.session["username"], request.session["name"]
        return RedirectResponse("/")
    else:
        #print("/signout endpoint was visited but no signin state found.")
        return RedirectResponse("/")


@app.post("/createMessage")
#create new message
async def create_message(request: Request, new_message_name: str | None = Form(None)):

    website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)
    website_db_cursor = website_db.cursor()

    cmd = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    website_db_cursor.execute(cmd, (request.session["member_id"],new_message_name))
    website_db.commit()
    #print("Added message!")
    return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)

@app.post("/deleteMessage")
#delete existing message
async def delete_message(request: Request, post_id: int | None = Form(None)):   

    website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)    
    website_db_cursor = website_db.cursor()
    
    cmd = "DELETE FROM message WHERE id = %s"
    website_db_cursor.execute(cmd,(post_id,))
    website_db.commit()
    #print("Deleted message!")
    return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)

#Week7 New: API for Member
#Try Swagger UI
#try environment variables => done
@app.get("/api/member")
async def query_member_api(request: Request, username: str):
    #first check login state.
    #1. login state NG: response None(python)/null(js)
    if "member_id" not in request.session or request.session["member_id"] == None:
        result_dict={"data":None}
        return JSONResponse(content=result_dict)
    
    #2. login state OK: MySQL SELECT data
    else:
        website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)    
        website_db_cursor = website_db.cursor()
    
        cmd = "SELECT id, username, name FROM member WHERE username = %s"
        website_db_cursor.execute(cmd,(username,))
        website_db_result = website_db_cursor.fetchone()
        
        #2-1: if successfully SELECT data: response with that data (json format)
        if website_db_result != None:
            result_dict={"data":{}}
            result_dict["data"]["id"] = website_db_result[0]
            result_dict["data"]["name"] = website_db_result[2]
            result_dict["data"]["username"] = website_db_result[1]
            return JSONResponse(content=result_dict)
        
        #2-2: if unsuccessful: return None(python)/null(js)
        else:
            result_dict={"data":None}
            return JSONResponse(content=result_dict)


@app.patch("/api/member")
#Week7 new: Add a feature to edit usaername by "PATCH" method
#Created data model "NewUsername" reference FastAPI request body: https://fastapi.tiangolo.com/tutorial/body/
async def username_change_api(request: Request, new_username: NewUsername):
    result_dict_ok={"ok":True}
    result_dict_error={"error":True}
    #case: user is not signed in
    if "member_id" not in request.session or request.session["member_id"] == None:
        return JSONResponse(content=result_dict_error)
    #case: username is empty or all blanks
    elif len(new_username.name) == 0 or new_username.name.isspace():        
        return JSONResponse(content=result_dict_error)
    else:
        try:
            website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)    
            website_db_cursor = website_db.cursor()
            cmd = "UPDATE member SET name = %s WHERE id = %s"
            website_db_cursor.execute(cmd,(new_username.name,request.session["member_id"]))
            website_db.commit()
            return JSONResponse(content=result_dict_ok)
        except Exception as error:
            print(error)
            return JSONResponse(content=result_dict_error)

@app.get("/xssTrial")
# main page renders login.html template.
async def xss_trial(request: Request):
    return templates.TemplateResponse("test1.html", {"request": request})

@app.get("/fetchTrial")
# main page renders login.html template.
async def fetch_trial(request: Request):
    return templates.TemplateResponse("task4fetch.html", {"request": request})

@app.post("/postTrial")
#post request trial
async def post_trial(request: Request, response: Response):
    result_dict_ok={"ok":True}
    #method one
    #response.headers["Access-Control-Allow-Origin"]= "http://127.0.0.1:8052"
    #response.headers["Response-PLY"] = "PLY"
    #return result_dict_ok

    #method two
    result_headers = {"Access-Control-Allow-Origin":"http://127.0.0.1:8052", "Response-PLY":"PLY"}
    return JSONResponse(content=result_dict_ok, headers=result_headers)

    #method three
    #use import CORSMiddleware

@app.get("/nodefer")
# main page renders login.html template.
async def async_defer_trial(request: Request):
    return templates.TemplateResponse("task1nodefer.html", {"request": request})


@app.get("/withdefer")
# main page renders login.html template.
async def async_defer_trial(request: Request):
    return templates.TemplateResponse("task1withdefer.html", {"request": request})

"""
DB Schemas:
(1) Table "member"
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| id       | int          | NO   | PRI | NULL    | auto_increment |
| username | varchar(255) | NO   |     | NULL    |                |
| password | varchar(255) | NO   |     | NULL    |                |
| name     | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+

(2) Table "message"
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | bigint       | NO   | PRI | NULL              | auto_increment    |
| member_id  | bigint       | NO   |     | NULL              |                   |
| content    | varchar(255) | NO   |     | NULL              |                   |
| like_count | int unsigned | NO   |     | 0                 |                   |
| time       | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+

"""