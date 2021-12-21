import logging
import tornado.web
from api_handler.const import API_HANDLER_OK_CODE


class BaseHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes):
        pass

    def set_default_headers(self):
        # The following allow all origins and all methods.
        # Modify according to your application (or leave it as-is at your own risk)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', '*')

    def reply_client(self, status_code: int, data: dict):
        if status_code != API_HANDLER_OK_CODE:
            logging.error(f"BaseHandler::reply_client - error {status_code}")
            self.send_error(status_code)
        else:
            self.write(data)
