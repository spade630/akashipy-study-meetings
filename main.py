from bottle import route, run, template
import requests

@route('/')
def index():
    return '<b>Hello World!</b>\n<a href=\"./events\">Events?</a>'

@route('/hello')
def index():
    return template('hello', name='ゆーり')

@route('/events')
def events():
    r = requests.get('http://connpass.com/api/v1/event/?keyword=python')
    return template('events', events=r.json()['events'][:10])

run(host='localhost', port=8080, debug=True, reloader=True)