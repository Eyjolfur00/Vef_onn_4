from bottle import *
import os

@route("/")
def index():
    return"hallo heimur"

run(host="0.0.0.0", port=os.environ.get("PORT"))
#run(host="localhost", port8080)
