import connexion
import six

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.models.selection import Selection  # noqa: E501
from swagger_server import util


def course_by_id(course_id):  # noqa: E501
    """Get a specific course by ID

     # noqa: E501

    :param course_id: 
    :type course_id: int

    :rtype: Course
    """
    return 'do some magic!'


def destroy_selection(student, course):  # noqa: E501
    """Destroy a selection

     # noqa: E501

    :param student: 
    :type student: int
    :param course: 
    :type course: int

    :rtype: None
    """
    return 'do some magic!'


def insert_selection(student, course):  # noqa: E501
    """Create a selection

     # noqa: E501

    :param student: 
    :type student: int
    :param course: 
    :type course: int

    :rtype: None
    """
    return 'do some magic!'


def selection_by_student(student_id):  # noqa: E501
    """Get a student&#x27;s selections

     # noqa: E501

    :param student_id: 
    :type student_id: int

    :rtype: Selection
    """
    return 'do some magic!'
