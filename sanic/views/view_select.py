from sanic.response import json,HTTPResponse
from sanic.request import Request
from common.wechatpicture import PictureSpider

async def get_image(request:Request) -> HTTPResponse:

    url=request.json.get('url')

    Spider=PictureSpider(url)
    link=Spider.get_pictures()

    return json(link)

