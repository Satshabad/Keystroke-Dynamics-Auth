import bottle
from bottle import route, run, request, static_file

@route('/getConfidence', method='POST')
def getConfidence():
    keyStrokeData = request.json
    print keyStrokeData

@route('/generate', method='GET')
def servePage():
    return(open('test1.html').read())

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

run()
