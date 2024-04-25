from fastapi import FastAPI, Request, Form, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

#Templates - FastAPI https://fastapi.tiangolo.com/advanced/templates/ & https://fastapi.tiangolo.com/reference/templating/
templates = Jinja2Templates(directory="templates")

#creates a webapp
app = FastAPI()
#增加一個SessionMiddleWare("中間件"?)來處理session. #need to install "itsdangerous" library
app.add_middleware(SessionMiddleware, secret_key="LoremIpsumSakuraMirage", max_age=None)
#Static(靜態) files - 可以不執行程式，直接將檔案傳送到前端的檔案。例如，html, css等。 https://fastapi.tiangolo.com/tutorial/static-files/
app.mount("/static", StaticFiles(directory="static"), name="static")

Request.session = {}

@app.get("/")
#要加async的原因: https://medium.com/@neeraztiwari/understanding-sync-vs-async-rest-apis-with-fastapi-a-comparative-guide-e8e95579db44
#async = asynchronous, CPU在做一件事情的時候同步可以做另一件事。常搭配await關鍵字。
#不加的話，就會等這件事做完再開始做下一件事，如果要做的事情要花30分鐘，那程式就會卡30分鐘......
async def index(request: Request, sign_in_state: bool | None = None):
    #task 3 part
    if "signed_in" not in request.session:
        request.session["signed_in"] = False         
    #print(request.session)
    #ValueError: context must include a "request" key => TemplateResponse裡面一定要有"request"的key, request: "something" (something不能隨便亂填像"333"的東西，一定要是Request object)
    return templates.TemplateResponse("login.html", {"request": request, "sign_in_state": request.session["signed_in"]})

@app.get("/error")
async def loginerror(request: Request, message: str | None = None):
    return templates.TemplateResponse("loginerror.html", {"request": request, "message": message})

@app.get("/member")
async def loginsuccess(request: Request):
    if "signed_in" not in request.session:
        #print("Session has no sign_in info, redirecting to login form...")
        return RedirectResponse("/")
    elif request.session["signed_in"] == False:
        #print("Access without login state detected!")
        return RedirectResponse("/")
    else:
        return templates.TemplateResponse("loginsuccess.html", {"request": request, "sign_in_state": request.session["signed_in"]})

#POST跟GET的不同?
@app.post("/signin")
#async def check_credentials(request: Request, username_name: str | None = Form(...), password_name: str | None = Form(...)):
#In the above code, The ... in Form(...) means something is required. FastAPI then returns a error.
#but here we want to redirect instead of a FastAPI error, therefore I make it "not required" but set a default value of None.
async def check_credentials(request: Request, username_name: str | None = Form(None), password_name: str | None = Form(None)):
    if username_name == None or password_name == None:
        return RedirectResponse("/error?message=請輸入帳號與密碼 Please enter username and password", status_code=status.HTTP_303_SEE_OTHER)
    if username_name == "test" and password_name == "test":
        request.session["signed_in"] = True
        #print(request.session)
        #POST轉GET需要status_code=status.HTTP_303_SEE_OTHER ... 查一下細節
        return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse("/error?message=帳號、或密碼輸入錯誤 Username or password is not correct", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/signout")
async def signout(request: Request):
    #print(request.session)
    request.session["signed_in"] = False
    #print(request.session)
    return RedirectResponse("/")

#get method
#changed to javascript version per assignment task 4 spec 3...
"""
@app.get("/square")
async def square(request: Request, the_integer: int):
    #print(request.session, the_integer)
    return RedirectResponse(f"/square/{the_integer}")
"""

@app.get("/square/{the_integer}")
async def print_square(request: Request, the_integer: int):
    return templates.TemplateResponse("square.html", {"request": request, "result": the_integer ** 2})