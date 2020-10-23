import logging
import pandas as pd
from database.data_models import PredModel
from utils.db_utils import save_to_db
from sqlalchemy.orm.session import Session


def build_dataframe(data: list, stores: dict):
    df = pd.DataFrame(data)
    df['dates'] = pd.to_datetime(df['created_at'])
    df['weekday'] = df['dates'].dt.weekday_name
    df['store'] = df.store_id.map(stores)
    df = df.fillna({'store': 6})
    df = df.loc[:, ('order_id', 'store', 'to_user_distance', 'to_user_elevation', 'total_earning', 'weekday'), ]
    return df


class takenPrediction:
    def __init__(self, model):
        self.__model = model['model']
        self.__preprocessor = model['preprocessing']
        self.stores = model['stores']

    def predict(self, session: Session, data: list) -> dict:
        logging.info('Predict start')
        df = build_dataframe(data, stores=self.stores)
        logging.info('Preprocessing data')
        data_pre = self.__preprocessor.transform(df)
        logging.info('Predict taken')
        prediction = self.__model.predict_proba(data_pre)[:, 1]

        response = dict()
        for i in range(0, len(data)):
            aux = dict()
            taken_prob = prediction[i]
            aux['order_id'] = data[i]['order_id']
            aux['store_id'] = data[i]['store_id']
            aux['to_user_distance'] = data[i]['to_user_distance']
            aux['to_user_elevation'] = data[i]['to_user_elevation']
            aux['total_earning'] = data[i]['total_earning']
            aux['order_date'] = data[i]['created_at']
            aux['taken_probability'] = taken_prob.astype(float)

            new_row = PredModel(**aux)
            save_to_db(session=session, db_model=new_row)
            response.update({data[i]['order_id']: taken_prob.astype(float)})

        return response
