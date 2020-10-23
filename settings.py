import os
import datetime as dt

APP_VERSION = "1.0.0"

APP = 'prediction-taken'
DEPLOYED_AT = dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
DEBUG = os.getenv('DEBUG', True)
PROPAGATE_EXCEPTIONS = os.getenv('PROPAGATE_EXCEPTIONS', True)

BASE_PATH = f"/api/{APP}"

LOG_PATTERN = '%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s'

# MODEL
MODEL_PATH = f'./models/modelTest.pickle'

# PostgreSQL
PG_USER = os.getenv('PG_USER', 'postgres')
PG_PASSWORD = os.getenv('PG_PASSWORD', 'postgres')
PG_HOST = os.getenv('PG_HOST', 'localhost')
PG_PORT = os.getenv('PG_PORT', 5432)
PG_DATABASE = os.getenv('PG_DATABASE', 'postgres')

# Waitress Config
PORT = int(os.getenv('PORT', 8080))
WAITRESS_WORKERS = int(os.getenv('WAITRESS_WORKERS', 8))
WAITRESS_CHANNELS = int(os.getenv('WAITRESS_CHANNELS', 300))
