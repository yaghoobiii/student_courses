from swagger_server.models.login_status import LoginStatus  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def login(user_id, password):  # noqa: E501
    """Login interface for students

     # noqa: E501

    :param user_id:
    :type user_id: str
    :param password:
    :type password: str

    :rtype: LoginStatus
    """
    return LoginStatus(password, User(int(user_id), "Ghazanfar", 0))
