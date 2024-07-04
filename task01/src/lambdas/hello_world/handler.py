from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        _LOG.info(f"Received event: {event} \t {repr(event)}")
        _LOG.info(f"Received context: {context} \t {repr(context)}")
        return {
            "statusCode": 200,
            "message": "Hello from Lambda"
        }
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
