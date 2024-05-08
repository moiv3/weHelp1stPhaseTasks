from fastapi import FastAPI, Request, Form, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

import mysql.connector

#database parameters
db_host="localhost"
db_user="brian"
db_pw="password2000mei"
db_database="website"

#sessionMiddleWare secret key parameter
session_secret_key="RAGEfeatH14ofLEONAIR"

#Templates - FastAPI https://fastapi.tiangolo.com/advanced/templates/ & https://fastapi.tiangolo.com/reference/templating/
templates = Jinja2Templates(directory="templates")

#creates a webapp
app = FastAPI()

#Don't forget SessionMiddleware...忘了這個於是debug了許久orz
app.add_middleware(SessionMiddleware, secret_key=session_secret_key, max_age=None)

#mount the static files. without this css and js don't work
app.mount("/static", StaticFiles(directory="static"), name="static")

#TODO: try cookies instead of request.session?

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
        website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)

        #sql queries
        website_db_cursor = website_db.cursor()
        #member id & message id for task 6
        cmd = "SELECT member.name, message.content, member.id, message.id FROM message JOIN member ON message.member_id = member.id"
        website_db_cursor.execute(cmd)
        website_db_result = website_db_cursor.fetchall()
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
        #print("/signout was visited but no signin state found.")
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