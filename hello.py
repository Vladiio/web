

def wsgi_application(environ, start_response):
    status = "200 OK"
    qs = environ.get('QUERY_STRING', '')
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    body = bytes('\n'.join(qs.split('&')), 'utf-8')
    with open('text.txt', 'wb') as file:
        file.write(body)
    return [body]

