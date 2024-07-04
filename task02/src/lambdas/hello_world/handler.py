from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        method = event['httpMethod']
        path = event['path']
        _LOG.info(f"Received event: {event} \t {repr(event)}")
        _LOG.info(f"Received context: {context} \t {repr(context)}")
        _LOG.info(f"HTTP Method: {method}")
        _LOG.info(f"Path: {path}")
        return {
            "statusCode": 200,
            "message": "Hello from Lambda"
        } if '/hello' == path.lower() and 'get' == method.lower() else {
            "statusCode": 400,
            "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
        }


HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
