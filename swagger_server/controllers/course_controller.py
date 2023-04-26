from typing import List

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.util import db


def course_by_id(course_id, token):  # noqa: E501
    """Get a specific course by ID

     # noqa: E501

    :param course_id:
    :type course_id: int
    :param token:
    :type token: str

    :rtype: Course
    """
    i = db.cursor().execute("SELECT * FROM course WHERE id = ?", [course_id]).fetchone()
    return Course(i[0], i[1], i[2], i[3], i[4], i[5])  # util.deserialize_model(i, Course)


def courses(token):  # noqa: E501
    """Get all the courses

     # noqa: E501

    :param token:
    :type token: str

    :rtype: List[Course]
    """
    ret: List[Course] = list()
    for i in db.cursor().execute("SELECT * FROM course").fetchall():
        ret.append(Course(i[0], i[1], i[2], i[3], i[4], i[5]))
    return ret
