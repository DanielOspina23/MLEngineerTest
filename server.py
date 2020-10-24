import logging
import json
from flask import Flask, request, Response
import datetime as dt
from database.db import engine, Base, connection_uri, create_session
import settings
import routes
from utils.exception_utils import handle_exception, request_logger
from waitress import serve
from entities.prediction_request import predictionRequest
from services.load_model import LoadModel
from services.prediction_model import takenPrediction


# APP init config
app = Flask(__name__)
app.config["DEBUG"] = settings.DEBUG
app.config["SQLALCHEMY_DATABASE_URI"] = connection_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = settings.PROPAGATE_EXCEPTIONS
app.config['SQLALCHEMY_POOL_RECYCLE'] = 120


# Logs
logging_mode = logging.INFO
logging.basicConfig(format=settings.LOG_PATTERN, level=logging_mode)

Base.metadata.create_all(bind=engine)

model_loader = LoadModel(path=settings.MODEL_PATH)
model = model_loader.load()

taken_model = takenPrediction(model=model)


# Status endpoint
@app.route(routes.STATUS, methods=['GET'])
def health_check():
    return Response(response=json.dumps({
        'msg': 'Up and running',
        'version': settings.APP_VERSION,
        'deployed at': settings.DEPLOYED_AT,
        'requested at utc': dt.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
    }),
        headers={"Content-Type": "application/json"},
        status=200)


@app.route(routes.GET_PREDICTION, methods=['POST'])
def get_prediction():
    request_logger(requests=request)
    try:
        req = request.json

        for r in req:
            predictionRequest.validate_request(r)
        session = create_session(engine_object=engine)
        result = taken_model.predict(session=session, data=req)
        return json.dumps(result)

    except Exception as e:
        request_logger(requests=request)
        return handle_exception(e)


if __name__ == "__main__":
    logger = logging.getLogger('waitress')
    logging.info('Server started.')
    serve(
        app=app,
        host='0.0.0.0',
        port=settings.PORT,
        threads=settings.WAITRESS_WORKERS,
        connection_limit=settings.WAITRESS_CHANNELS
    )
