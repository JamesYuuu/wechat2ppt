from urllib.request import Request
from sanic import Sanic
from sanic_ext import Extend
from routes import add_route

app=Sanic('MyAppServer')
Extend(app)
add_route(app)
app.run(host='0.0.0.0',port=8000,debug=True)