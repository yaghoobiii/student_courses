import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder
from swagger_server.util import create_db


class BaseTestCase(TestCase):

    def create_app(self):
        create_db()
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
