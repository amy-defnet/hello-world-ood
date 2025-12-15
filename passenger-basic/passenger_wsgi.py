# passenger_wsgi.py
import sys


def application(environ, start_response):
    start_response("200 OK", [("Content-type", "text/plain")])
    return ["Hello World from Open OnDemand (Python WSGI)!\n\n" + sys.version]
