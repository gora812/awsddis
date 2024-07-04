from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass

    def handle_request(self, event, context):
        method = _read(event, 'requestContext', 'http', 'method')
        path = _read(event, 'requestContext', 'http', 'path')
        _LOG.info(f"Received event: {event} \t {repr(event)}")
        _LOG.info(f"Received context: {context} \t {repr(context)}")
        _LOG.info(f"HTTP Method: {method}")
        _LOG.info(f"Path: {path}")
        if '/hello' == path.lower() and 'get' == method.lower():
            return {
                "statusCode": 200,
                'body': {
                    "statusCode": 200,
                    "message": "Hello from Lambda"
                }}
        else:
            return {
                "statusCode": 400,
                'body': {
                    "statusCode": 400,
                    "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
                }}


HANDLER = HelloWorld()


def _read(data, *keys):
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return None
    return data


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
