import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get the environment variable
        env_value = os.getenv('MY_ENV_VAR', 'Variable not set')

        # Log the environment variable
        print(f"MY_ENV_VAR: {env_value}")

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send the environment variable as a response
        response = f"<html><body><h1>ENV_VARIABLE_NAME: {env_value}</h1></body></html>"
        self.wfile.write(response.encode('utf-8'))

if __name__ == '__main__':
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Server running on port {port}")
    httpd.serve_forever()
