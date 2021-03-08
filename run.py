import os
import unittest

from app.main import create_app, db
from app import blueprint

from logging.config import fileConfig

# get config from env for 'prod', 'dev' or 'test', if none then defaults to 'dev'
app = create_app(os.getenv('APP_ENV') or 'prod')
fileConfig("logging.cfg")
app.register_blueprint(blueprint)
app.app_context().push()

if __name__=='__main__':
    app.run(host='0.0.0.0')