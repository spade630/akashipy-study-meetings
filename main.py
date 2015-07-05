from bottle import route, run, template, request
import requests

@route('/')
def index():
    return template('hello', name="Python")
    #return '<b>Hello World!</b>\n<a href=\"./events\">Events?</a>'

@route('/hello')
def index():
    return template('hello', name='hoge')

@route('/events')
def events():
    keyword=request.query.keyword
    r = requests.get('http://connpass.com/api/v1/event/?keyword='+keyword)
    return template('events', events=r.json()['events'][:10])

@route('/events/<keyword>')
def events(keyword):
    r = requests.get('http://connpass.com/api/v1/event/?keyword='+keyword)
    return template('events', events=r.json()['events'][:10])

from os import environ
if environ.get('IS_HEROKU'):
    run(server='gunicorn', host='0.0.0.0', port=int(environ.get("PORT",5000)))
else:
    run(host='localhost', port=8080, debug=True, reloader=True)