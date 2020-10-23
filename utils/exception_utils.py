import json
import logging
from flask import Response, request
from validx.exc.errors import SchemaError
from flask.wrappers import BadRequest


def handle_exception(exception: Exception):
    try:
        raise exception
    except BadRequest as ex:
        logging.info(f'Exception 400')
        return Response(response=json.dumps({'msg': str(ex.description)}),
                        headers={'Content-Type': 'application/json'},
                        status=400)
    except SchemaError as ex:
        logging.info(f'Exception 400')
        return Response(response=json.dumps({'msg': str(ex.errors)}),
                        headers={'Content-Type': 'application/json'},
                        status=400)
    except Exception as ex:
        log = {'Content-Type': 'application/json'}
        logging.info(f'Exception 500')
        logging.exception(ex)
        return Response(response=json.dumps({'msg': f'Server Error: {repr(ex)}'}),
                        headers={'Content-Type': 'application/json'},
                        status=500)


def request_logger(requests: request) -> None:
    application_id = requests.headers.get('X-Application-Id', 'Unknown Source')
    logging.info(f'Incoming requests from: {application_id}')
