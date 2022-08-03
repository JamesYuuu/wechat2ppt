from sanic import Sanic
from sanic_ext import Extend
from routes import add_route

app=Sanic('MyAppServer')
Extend(app)
add_route(app)

app.static("/", "./dist")
app.static("/","./dist/index.html")

app.config.RESPONSE_TIMEOUT=90

app.run(host='0.0.0.0',port=8000)
