import tornado.web
from api_handler.api_handler import ServiceHandler


class APIWebApp(tornado.web.Application):
    def __init__(self):
        # Define the handlers answering requests from clients
        self.handlers = [
            # Add all the endpoints here
            (r"/api_endpoint", ServiceHandler),
        ]
        super(APIWebApp, self).__init__(self.handlers)
