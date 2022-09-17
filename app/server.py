import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from app.get_properties import GetProperties


class Server(BaseHTTPRequestHandler):
    def _set_headers(self, status_code):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        try:
            properties = GetProperties(self.path).filtered_properties()
            if properties:
                response = bytes(json.dumps(properties), 'utf-8')
                self._set_headers(status_code=200)
                self.wfile.write(response)
            else:
                self._set_headers(status_code=404)
                message = {'message': 'Not properties found'}
                response = bytes(json.dumps(message), 'utf-8')
                self.wfile.write(response)
        except Exception as e:
            self._set_headers(status_code=500)
            self.wfile.write(f"Error: {e}")


def run(server_class=HTTPServer, handler_class=Server, port=8000):
    server_address = ('', port)
    http_server = server_class(server_address, handler_class)

    print('Starting http server on port %d...' % port)
    http_server.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
