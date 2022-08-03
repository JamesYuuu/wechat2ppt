from turtle import width
from urllib import response
from sanic.request import Request
from sanic.response import HTTPResponse
from sanic import response
from common.picture2ppt import make_ppt
import os

async def download(request: Request) -> HTTPResponse:
    
    width=request.json.get('width')
    ratio=request.json.get('ratio')
    make_ppt(width,ratio)
    
    return await response.file_stream('image/result.pptx')
