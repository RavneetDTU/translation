from http import HTTPStatus
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, Response, requests, status

from pydantic import BaseModel

from config.config import MySQLSettings, Settings
from common.pinject.container import Container
from controller.translation_controller import TranslationController
from controller.auth_controller import AuthController
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class TranslateRequest(BaseModel):
    input_text: str
    input_language: Optional[str] = None
    output_language: str


class TranslateResponse(BaseModel):
    translation_id: int
    translated_text: str
    confidence_score: float


# @app.middleware("http")
# async def before_after_requests(request: Request, call_next):
#     response = await call_next(request)
#     Container(MySQLSettings.get_settings())
#     container = Container.get_object_graph()
#     ss = container.provide(SqlAlchemySessionServiceProvider)
#     ss.session().commit()
#     return response


async def verify_token(token: str = Depends(oauth2_scheme)):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    auth_controller = container.provide(AuthController)
    user, error = auth_controller.verify_token(token)
    if error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=error,
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@app.post("/translate", response_model=TranslateResponse)
async def translate(translate: TranslateRequest, user=Depends(verify_token)):
    Container(Settings.get_settings())
    import ipdb; ipdb.set_trace()
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    res = translation_controller.get_translation(translate, user)
    return res


class SuggestionRequest(BaseModel):
    translation_id: int
    suggested_text: str


@app.post("/suggestion", status_code=HTTPStatus.NO_CONTENT)
async def suggestion(suggestion: SuggestionRequest, user=Depends(verify_token)):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    error = translation_controller.add_suggestion(suggestion, user)
    if error:
        raise HTTPException(status_code=400, detail={"message": error})
    return Response(status_code=HTTPStatus.NO_CONTENT.value)


class User(BaseModel):
    name: str
    email: str
    password: str


@app.post("/register", status_code=HTTPStatus.NO_CONTENT)
async def login(user: User):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    auth_controller = container.provide(AuthController)
    error = auth_controller.register_user(user)
    if error:
        raise HTTPException(status_code=400, detail={"message": error})
    return Response(status_code=HTTPStatus.NO_CONTENT.value)


class Token(BaseModel):
    access_token: str
    token_type: str


@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    auth_controller = container.provide(AuthController)
    data, error = auth_controller.login_user(form_data)
    if error:
        raise HTTPException(status_code=401, detail={"message": error})
    return data
