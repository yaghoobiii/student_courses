import connexion
from flask import send_from_directory

from swagger_server import encoder
from swagger_server.util import create_db


def es6_static(full_path: str):
    if '.' not in full_path or full_path.endswith(".min"):
        return send_from_directory(
            "../swagger_client/js", full_path + ".js", as_attachment=True, mimetype='text/javascript')
    else:
        return send_from_directory("../swagger_client/js", full_path)


def main():
    create_db()
    app: connexion.App = connexion.App(__name__, specification_dir='./swagger/', server_args={
        'static_url_path': '', 'static_folder': '../swagger_client'})
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'student-courses'}, pythonic_params=True)
    app.add_url_rule('/js/<path:full_path>', 'js', es6_static)
    app.run(port=8080)


if __name__ == '__main__':
    main()
