from fastapi import FastAPI, Request, Form, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="LoremIpsumSakuraMirage", max_age=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

Request.session = {}

@app.get("/")
async def index(request: Request, sign_in_state: bool | None = None):
    #html_file = open("index.html", 'r', encoding="utf-8").read()
    #return HTMLResponse(content=html_file, status_code=200)
    print(request.session)
    if "signed_in" not in request.session:
         request.session["signed_in"] = False         
    print(request.session)
    return templates.TemplateResponse("login.html", {"request": request, "sign_in_state": request.session["signed_in"]})

@app.get("/error")
async def loginerror(request: Request, message: str | None = None):
    return templates.TemplateResponse("loginerror.html", {"request": request, "message": message})

@app.get("/member")
async def loginsuccess(request: Request):
    if request.session["signed_in"] == False:
        print("Detected not login", request.session)
        return RedirectResponse("/")
    else:
        return templates.TemplateResponse("loginsuccess.html", {"request": request, "sign_in_state": request.session["signed_in"]})

#form的action = submit
@app.post("/signin")
async def check_credentials(request: Request, username_name: str | None = Form(...), password_name: str | None = Form(...), termsagreed_name: bool = Form(False)):
    if username_name == "test" and password_name == "test":
        #return success page?
        print(request.session)
        request.session["signed_in"] = True
        print(request.session)
        return RedirectResponse("/member", status_code=status.HTTP_303_SEE_OTHER)
    else:
        #return fail page?
        print(request.session)
        return RedirectResponse("/error?message=帳號、或密碼輸入錯誤", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/signout")
async def signout(request: Request):
        print(request.session)
        request.session["signed_in"] = False
        print(request.session)
        return RedirectResponse("/")

@app.get("/square")
async def square(request: Request, the_integer: int):        
        print(request.session, the_integer)
        return RedirectResponse(f"/square/{the_integer}")

@app.get("/square/{the_integer}")
async def print_square(request: Request, the_integer: int):
            return templates.TemplateResponse("square.html", {"request": request, "the_integer": the_integer, "result": the_integer ** 2, "sign_in_state": request.session["signed_in"]})