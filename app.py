from fastapi import FastAPI, Request
from database import get_post, insert_post
from models import Post, Posts
from sqlite3 import Connection, Row
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")


app = FastAPI()
connection = Connection('social.db')
connection.row_factory = Row

@app.get("/")
async def home(request: Request)-> HTMLResponse:
    return templates.TemplateResponse(
        request=request, name="./index.html", context={"id": id}
    )

@app.get("/posts")
async def posts()-> Posts:
    return get_post(connection)

@app.post("/post")
async def add_post(post : Post)-> Post:
    insert_post(connection,post)
    return post
