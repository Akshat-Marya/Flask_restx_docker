import uuid
import datetime

from ..config import key


from app.main import db
from app.main.model.house_model import Houses
from app.main.model.transaction_model import Transactions

from app.main.util.model_interface import HousePriceModel


def save_new_transaction(data):

    # check if length less than 13, raise error
    if len(data['X'])<13 or len(data['X'])>13:
        response_object = {
            'status':'fail',
            'message': 'Input is invalid, formatting issues with input, Required: [feature1,feature2,feature2,feature3,feature4,feature1,....feature13]',
        }
        return response_object, 501
    try: 
        house = Houses(
                crim = data['X'][0],
                zn = data['X'][1],
                indus = data['X'][2],
                chas = data['X'][3],
                nox = data['X'][4],
                rm = data['X'][5],
                age = data['X'][6],
                dis = data['X'][7],
                rad = data['X'][8],
                tax = data['X'][9],
                ptratio =  data['X'][10],
                b = data['X'][11],
                lstat = data['X'][12]
        )
        transaction = Transactions(for_house=house)

        db.session.add(house)
        db.session.add(transaction)
        db.session.commit()

        model = HousePriceModel()
        price=model.predict(data['X'])[0]

        response_object = {
            'status':'success',
            'price': f'{price}',
        }
    except Exception as e:
        response_object = {
            'status':'fail',
            'message': 'Input is invalid, formatting issues with input',
        }
        return response_object, 501
    return response_object, 200

