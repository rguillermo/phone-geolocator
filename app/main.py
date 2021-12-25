from pathlib import Path

from fastapi import FastAPI, responses, requests, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.phoneinfo import PhoneNumber
from app.shortcuts import render


BASEDIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASEDIR / 'templates'
STATIC_DIR = BASEDIR / 'static'
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))




app = FastAPI()
app.mount('/static', StaticFiles(directory=STATIC_DIR), name='static')

def is_htmx(request: requests.Request) -> bool:
    return request.headers.get('hx-request') == 'true'


@app.get("/", response_class=responses.HTMLResponse)
async def home(request: requests.Request):
    context = {
        'request': request
    }
    return render('index.html', context)


@app.post("/phoneinfo")
async def phoneinfo(request: requests.Request, phonenumber: str = Form(...)):
    context = {}
    context['data'] = PhoneNumber(phonenumber).info()
    context['request'] = request
    return render('snippets/phone_info.html', context)