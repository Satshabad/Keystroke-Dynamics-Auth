import bottle
from bottle import route, run, request, static_file

import userstore

@route('/getConfidence', method='POST')
def getConfidence():
    keyStrokeData = request.json
    data = []
    last_chr = ''
    for event in keyStrokeData['data']:
        if last_chr == '':
            last_chr = chr(event['keyCode'])
        else:
            data.append((last_chr + chr(event['keyCode']), event['flightTime']))
            last_chr = chr(event['keyCode'])

    userstore.createUser(keyStrokeData['userID'], data)

@route('/generate', method='GET')
def servePage():
    return(open('test1.html').read())

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./')

run()
