from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


fastapi_app = FastAPI(
    debug=True,
    title="Studio",
    version="0.0.1",
)

fastapi_app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@fastapi_app.get("/")
async def indexPage(request: Request) -> None:
    return templates.TemplateResponse(
        name="index.html",
        context={"request": request},
    )
