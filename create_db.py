import os
import unittest

import datetime

from app.main import create_app, db
from app.main.model.house_model import Houses
from app.main.model.transaction_model import Transactions
from app import blueprint

from logging.config import fileConfig

# get config from env for 'prod', 'dev' or 'test', if none then defaults to 'dev'
app = create_app(os.getenv('APP_ENV') or 'dev')
app.app_context().push()

# create db
db.drop_all()
db.create_all()