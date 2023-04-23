from typing import List

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.util import db


def courses():  # noqa: E501
    """Get all the courses

     # noqa: E501


    :rtype: List[Course]
    """
    ret: List[Course] = list()
    for i in db.cursor().execute("SELECT * FROM course").fetchall():
        ret.append(Course(i[0], i[1], i[2], i[3], i[4], i[5]))
    return ret
