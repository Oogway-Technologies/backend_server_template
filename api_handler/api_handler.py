import json
import logging
from api_handler.base_handler import BaseHandler
from api_handler.const import (API_HANDLER_ERROR_CODE, API_HANDLER_OK_CODE, SERVICE_HANDLER_POST_ARG_KEY,
                               SERVICE_HANDLER_POST_BODY_KEY)


class ServiceHandler(BaseHandler):
    """
    A general handler to respond to REST requests.
    The following shows only the implementation for a POST request.
    If you need GET, DELETE or PUT, their implementation is similar
    to the POST request below:
    def get(self):
        code here

    def delete(self):
        code here

    def put(self):
        code here
    """
    def post(self):
        """
        A POST request in which we assume there is an argument and a body.
        :return: None
        """
        # Get the argument
        try:
            key = self.get_argument(SERVICE_HANDLER_POST_ARG_KEY, default="", strip=True)
        except:
            logging.error(f"ServiceHandler - POST: missing key argument {SERVICE_HANDLER_POST_ARG_KEY}")
            self.reply_client(status_code=API_HANDLER_ERROR_CODE, data={})
            return

        # Load the body of the post request
        try:
            req_body = json.loads(self.request.body)
            body_value = req_body[SERVICE_HANDLER_POST_BODY_KEY]
        except:
            logging.error(f"ServiceHandler - POST: error while reading the body for {SERVICE_HANDLER_POST_BODY_KEY}")
            self.reply_client(status_code=API_HANDLER_ERROR_CODE, data={})
            return

        # Reply back to client with a map
        data = {
            'key': key,
            'body_value': body_value
        }
        self.reply_client(status_code=API_HANDLER_OK_CODE, data=data)
