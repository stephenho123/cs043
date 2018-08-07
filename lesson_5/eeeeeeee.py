import wsgiref.simple_server

import http.cookies

def application(environ, start_response):

    headers = [('Content-Type', 'text/plain; charset=utf-8'),

        ('Set-Cookie: favoriteAnimal=Dog'),

        ('Set-Cookie: favoriteNumber=4'),

        ('Set-Cookie: favoriteColor=red')]


    start_response('200 OK', headers)

#response…

httpd = wsgiref.simple_server.make_server('', 8000, application)

httpd.serve_forever()