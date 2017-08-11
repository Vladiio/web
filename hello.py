import json


def wsgi_application(environ, start_response):
    status = "200 OK"
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    body = 'Hello world'
    return [body]

