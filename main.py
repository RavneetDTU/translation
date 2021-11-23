from typing import Optional

from fastapi import FastAPI, Request

from pydantic import BaseModel

from config.config import MySQLSettings
from common.pinject.container import Container
from controller.translation_controller import TranslationController
from common.pinject.sql_alchemy_session_service_provider import SqlAlchemySessionServiceProvider

app = FastAPI()


class TranslateRequest(BaseModel):
    input_text: str
    input_language: Optional[str] = None
    output_language: str


class TranslateResponse(BaseModel):
    translation_id: int
    translated_text: str
    confidence_score: float


@app.middleware("http")
async def before_after_requests(request: Request, call_next):
    response = await call_next(request)
    Container(MySQLSettings.get_settings())
    container = Container.get_object_graph()
    ss = container.provide(SqlAlchemySessionServiceProvider)
    ss.session().commit()
    return response


@app.post("/translate", response_model=TranslateResponse)
async def translate(translate: TranslateRequest):
    Container(MySQLSettings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    res = translation_controller.get_translation(translate)
    return res
