#!/usr/bin/python3

import http.server
import json


"""Module providing a simple HTTP server with multiple endpoints.

This module defines an HTTP request handler class that responds to 
GET requests at specific paths like root data status and not found 
returning appropriate JSON or text content."""


class handler(http.server.BaseHTTPRequestHandler):
    """HTTP Request Handler for serving static-like responses
    via API endpoints.

    This subclass handles incoming GET requests by checking the
    path variable against known routes returns 200 OK with relevant
    payload or 404 Not Found if no matching route exists in this logic flow."""


    def do_GET(self):
        # Handles root endpoint "/" returning a simple 
        # welcome message page text content.
        if self.path == "/":
            self.send_response(200, "Main page")
            self.send_header("Content-Type","text")
            self.end_headers()
            self.wfile.write(b"Hello ! This is a simple API !")
            return

        # Handles data endpoint "/data" returning
        # static JSON object with user details.
        if self.path == "/data":
            data: dict = {"name": "John", "age": 30, "city": "New York"}
            payload: bytes = json.dumps(data).encode("utf-8")
            self.send_response(200, "data page")
            self.send_header("Content-Type","application/json")
            self.send_header("Content_Lenght", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return

        # Handles status endpoint "/status" returning
        # short text message indicating OK state.
        if self.path == "/status":
            status:str = "OK"
            lenght = status.encode("utf-8")
            self.send_response(200, "status page")
            self.send_header("Content-Type", "text")
            self.send_header("Content_Lenght",str(len(lenght)))
            self.end_headers()
            self.wfile.write(status.encode("utf-8"))
            return

        # Handles any unmatched path by returning
        # 404 error message indicating endpoint missing.
        else:
            error_message: str = "Endpoint not found"
            error_lenght = error_message.encode("utf-8")
            self.send_response(404, "Endpoint not found")
            self.send_header("Content-Type", "text")
            self.send_header("Content-Lenght", str(len(error_lenght)))
            self.end_headers()
            self.wfile.write(error_message.encode("utf-8"))
            return
            

my_server = http.server.HTTPServer(("", 8000), handler)
my_server.serve_forever()