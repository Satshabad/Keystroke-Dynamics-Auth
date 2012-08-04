import bottle
from bottle import route, run, request

@route('/getConfidence', method='POST')
def getConfidence():
    keyStrokeData = request.json
run()
