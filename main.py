from bottle import route, run, template

@route('/')
def index():
    return '<b>Hello World!</b>\n<a href=\"./hello\">hello?</a>'

@route('/hello')
def index():
    return template('hello', name='ゆーり')

@route('/events')
def index():
    return template('events')

run(host='localhost', port=8080, debug=True, reloader=True)