import connexion

from swagger_server import encoder
from swagger_server.util import create_db


def main():
    create_db()
    app: connexion.App = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'student-courses'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
