from flask import request
from flask_restx import Resource

from ..util.dto import TransactionDto
from ..service.transaction_service import save_new_transaction

import json


api = TransactionDto.api
_transaction = TransactionDto.transaction


@api.route('')
class Transaction(Resource):

    @api.response(201, 'Transaction successfully created.')
    @api.doc('create a new transaction')
    @api.expect(_transaction, validate=True)
    def post(self):
        """Creates a new Transaction """
        data = request.json
        return save_new_transaction(data=data)
