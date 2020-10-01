from views import index
from cgi import parse_qs, escape

def app(environ, start_response):
        data = index(environ)
        print("inputs6 ----------------- ", environ['wsgi.input'].read())
        
        start_response("200 OK", [
            ("Content-Type", "text/html"),
            ("Content-Length", str(len(data)))
        ])        
        return iter([data])


if __name__ == '__main__':
    from gevent.pywsgi import WSGIServer
    WSGIServer(('', 8000),app, spawn=None).serve_forever()