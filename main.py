from fastapi import Depends, FastAPI

from config.config import MySQLSettings
from common.pinject.container import Container
from controller.translation_controller import TranslationController

app = FastAPI()


@app.get("/")
async def root(settings: MySQLSettings = Depends(MySQLSettings.get_settings)):
    Container(MySQLSettings.get_settings())
    container = Container.get_object_graph()
    translation_controller = container.provide(TranslationController)
    translation_controller.getTranslation()
    return settings
    # return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
