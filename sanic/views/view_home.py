from sanic.response import json,HTTPResponse
from sanic.request import Request
from common.wechatpicture import PictureSpider

async def home(request:Request) -> HTTPResponse:

    return json({'message':'OK'})