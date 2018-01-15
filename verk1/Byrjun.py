from bottle import *

@route("/")

def index():
    return "Hálló bottlepy"

run(host="localhost", port=8080)
