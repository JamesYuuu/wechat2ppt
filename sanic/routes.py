from sanic import Sanic
from views.view_select import get_image
from views.view_download import download

def add_route(app:Sanic):
    app.add_route(get_image,'/select',methods='POST')
    app.add_route(download,'/download',methods='POST')