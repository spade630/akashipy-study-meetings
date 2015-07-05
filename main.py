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

run(host='localhost', port=8080)