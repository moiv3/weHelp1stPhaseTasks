from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

def signin_check(username, password):
    if username == None or password == None:
        print("THIS")
        return FileResponse('error.html')
    print(username == None) # still False when empty
    print(password == None) # still False when empty
    website_db = mysql.connector.connect(host=db_host,user=db_user,password=db_pw,database=db_database)
    
    website_db_cursor = website_db.cursor()
    cmd = ("SELECT username, password FROM member WHERE username = %s")
    website_db_cursor.execute(cmd, (username,))
    fetched_data = website_db_cursor.fetchone()
    if fetched_data:
        if password == fetched_data[1]:
            print("check ok!")
            #session
            return FileResponse('memberpage.html')
        else:
            print("check ng! password mismatch")
            return FileResponse('error.html')

app = FastAPI()

app.mount("/staticfiles", StaticFiles(directory="static_files"), name="static")

#database parameters [Week7: changed to environment variables]
db_host=os.getenv("db_host")
db_user=os.getenv("db_user")
db_pw=os.getenv("db_pw")
db_database=os.getenv("db_database")



@app.get("/")
async def index_page(request: Request):
    return FileResponse('index.html')

@app.get("/signin")
async def index_page(request: Request, username: str|None, password: str|None):
    return signin_check(username,password)

@app.post("/signin")
async def index_page(request: Request, username: str|None = Form(None), password: str|None = Form(None)):
    return signin_check(username,password)

#add session

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