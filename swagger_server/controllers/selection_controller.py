from typing import List

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.models.selection import Selection  # noqa: E501
from swagger_server.util import db


def destroy_selection(student, course):  # noqa: E501
    """Destroy a selection

     # noqa: E501

    :param student: 
    :type student: int
    :param course: 
    :type course: int

    :rtype: None
    """
    db.cursor().execute("DELETE FROM selection WHERE student = ? AND course = ?", [student, course])
    return "ok"


def insert_selection(student, course):  # noqa: E501
    """Create a selection

     # noqa: E501

    :param student: 
    :type student: int
    :param course: 
    :type course: int

    :rtype: None
    """
    db.cursor().execute("INSERT INTO selection VALUES(?, ?)", [student, course])
    return "ok"


def selection_by_student(student_id):  # noqa: E501
    """Get a student's selections

     # noqa: E501

    :param student_id: 
    :type student_id: int

    :rtype: Selection
    """
    ret: List[Selection] = list()
    for i in db.cursor().execute("SELECT * FROM selection WHERE student = ?", [student_id]).fetchall():
        ret.append(Selection(i[0], i[1]))  # util.deserialize_model(i, Selection)
    return ret  # FIXME
