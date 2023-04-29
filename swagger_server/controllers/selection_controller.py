from typing import List

from swagger_server.models.selection import Selection  # noqa: E501
from swagger_server.util import db


def destroy_selection(student, course, token):  # noqa: E501
    """Destroy a selection

     # noqa: E501

    :param student: 
    :type student: int
    :param course: 
    :type course: int
    :param token:
    :type token: str

    :rtype: None
    """
    db.cursor().execute("DELETE FROM selection WHERE student = ? AND course = ?", [student, course])
    db.commit()
    return "ok"


def insert_selection(student, course, token):  # noqa: E501
    """Create a selection

     # noqa: E501

    :param student: 
    :type student: int
    :param course: 
    :type course: int
    :param token:
    :type token: str

    :rtype: None
    """
    db.cursor().execute("INSERT INTO selection VALUES(?, ?)", [student, course])
    db.commit()
    return "ok"


def selection_by_student(student_id, token):  # noqa: E501
    """Get a student's selections

     # noqa: E501

    :param student_id:
    :type student_id: int
    :param token:
    :type token: str

    :rtype: List[Selection]
    """
    ret: List[Selection] = list()
    for i in db.cursor().execute("SELECT * FROM selection WHERE student = ?", [int(student_id)]).fetchall():
        ret.append(Selection(i[0], i[1]))  # util.deserialize_model(i, Selection)
    return ret
