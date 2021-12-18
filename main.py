from http import HTTPStatus
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, Response, status, Request

from pydantic import BaseModel

from config.config import Settings
from common.pinject.container import Container
from common.pinject.sql_alchemy_session_service_provider import SqlAlchemySessionServiceProvider
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


@app.middleware("http")
async def before_after_requests(request: Request, call_next):
    response = await call_next(request)
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    ss = container.provide(SqlAlchemySessionServiceProvider)
    error = response.status_code > 299
    if not error:
        ss.session().commit()
    ss.session().close()
    return response


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


async def verify_admin(user=Depends(verify_token)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user


@app.post("/translate", response_model=TranslateResponse)
async def translate(translate_data: TranslateRequest, user=Depends(verify_token)):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    res, error = translation_controller.get_translation(translate_data, user)
    if error:
        raise HTTPException(status_code=400, detail={"message": error})
    return res


class SuggestionRequest(BaseModel):
    translation_id: int
    suggested_text: str


@app.post("/suggestion", status_code=HTTPStatus.NO_CONTENT)
async def suggestion(suggestion_data: SuggestionRequest, user=Depends(verify_token)):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    error = translation_controller.add_suggestion(suggestion_data, user)
    if error:
        raise HTTPException(status_code=400, detail={"message": error})
    return Response(status_code=HTTPStatus.NO_CONTENT.value)


class User(BaseModel):
    name: str
    email: str
    password: str


@app.post("/register", status_code=HTTPStatus.NO_CONTENT)
async def register(user: User):
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


class TranslatedCharacters(BaseModel):
    characters_translated: int


@app.get("/translated/{user_id:int}", response_model=TranslatedCharacters)
async def translated(user_id: int, start_time: int, end_time: int, admin=Depends(verify_admin)):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    res, error = translation_controller.get_translated_characters_by_user_id(user_id, start_time, end_time)
    if error:
        raise HTTPException(status_code=400, detail={"message": error})
    return res


@app.get("/translated/{source:str}/{target:str}/", response_model=TranslatedCharacters)
async def translated(source, target, start_time: int, end_time: int, admin=Depends(verify_admin)):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    res, error = translation_controller.get_translated_characters_by_input_output_language(source, target, start_time, end_time)
    if error:
        raise HTTPException(status_code=400, detail={"message": error})
    return res


class Status(BaseModel):
    status: str


@app.get("/status/{source:str}/{target:str}", response_model=Status)
async def status(source, target):
    Container(Settings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    res, error = translation_controller.get_model_status(source, target)
    if error:
        raise HTTPException(status_code=400, detail={"message": error})
    return res
