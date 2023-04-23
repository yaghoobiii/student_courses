import connexion
import six

from swagger_server.models.login_status import LoginStatus  # noqa: E501
from swagger_server import util


def login(password):  # noqa: E501
    """Login interface for students

     # noqa: E501

    :param password: 
    :type password: str

    :rtype: LoginStatus
    """
    # TODO
    vet: list[password] = list()
    vet.append(password("1","مریم یعقوبی","88522000","0"))
    vet.append(password("2", "سارا یاغی", "88522522", "0"))
    vet.append(password("3", "امیرحسن زاده", "55886445", "0"))
    vet.append(password("4", "پارسااسماعیلی", "55669888", "0"))
    vet.append(password("5", "سمیراآشوری", "31255569", "0"))
    vet.append(password("6", "حسن کریمی", "555869", "0"))
    vet.append(password("7", "هدی جنالی زاده","55698455","0"))

    return 'vet'
