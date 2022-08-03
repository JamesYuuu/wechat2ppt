from sanic.request import Request
from sanic.response import HTTPResponse
from sanic import response
from common.wechatpicture import PictureSpider
from common.picture2ppt import ppt

async def download(request: Request) -> HTTPResponse:
    
    url=request.json.get('url')

    Spider=PictureSpider(url)
    link=Spider.get_pictures()

    width=[item['width'] for item in link]
    ratio=[item['ratio'] for item in link]

    pptx=ppt(link,max(width,key=width.count),max(ratio,key=ratio.count))
    await pptx.make_ppt()

    return await response.file_stream('image/result.pptx')