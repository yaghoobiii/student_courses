from swagger_server.models.login_status import LoginStatus  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.util import db


def login(user_id, password):  # noqa: E501
    """Login interface for students

     # noqa: E501

    :param user_id:
    :type user_id: str
    :param password:
    :type password: str

    :rtype: LoginStatus
    """
    raw_user = db.cursor().execute("SELECT name, type FROM user WHERE id = ? AND password = ?", [user_id, password]) \
        .fetchone()
    if raw_user is not None:
        return LoginStatus(password, User(int(user_id), raw_user[0], raw_user[1]))
    else:
        return LoginStatus(None, None)
