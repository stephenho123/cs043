import wsgiref.simple_server
import http.cookies


def application(environ, start_response):
    if environ['PATH_INFO'] != '/count':
        start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
        return ['Unknown app {}'.format(environ['PATH_INFO']).encode()]

    if 'HTTP_COOKIE' in environ:
        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        if 'counter' in cookies:
            counter = int(cookies['counter'].value) + 1
        else:
            counter = 0
    else:
        counter = 0

    headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Set-Cookie', 'counter={}'.format(counter))
    ]

    start_response('200 OK', headers)
    return ['Counter = {}'.format(counter).encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()