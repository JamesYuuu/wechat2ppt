from sanic import Sanic
from views.view_select import get_image
from views.view_download import download
from views.view_home import home

def add_route(app:Sanic):
    app.add_route(get_image,'/select',methods=['POST','GET'])
    app.add_route(download,'/download')
    app.add_route(home,'/')