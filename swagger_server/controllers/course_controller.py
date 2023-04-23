import connexion
import six

from typing import List

from swagger_server.models.course import Course  # noqa: E501
from swagger_server import util


def courses():  # noqa: E501
    """Get all the courses

     # noqa: E501


    :rtype: List[Course]
    """
    # TODO
    ret: List[Course] = list()
    ret.append(Course("20:00", "1", "ریاضی", "18:30", "مریم یزدی ", "5"))
    ret.append(Course("17:00", "2", "شبکه", "15:00", "رامین یزدی ", "4"))
    ret.append(Course("14:00", "3", "مهندسی نرم افزار", "12:00", "یاسر رستمی ", "1"))
    ret.append(Course("9:00", "4", "داده کاوی", "9:00", "مرضیه بهرامی ", "2"))
    ret.append(Course("13:00", "5", "اصول طراحی سیستم", "11:00", "ارسلان کریمی ", "5"))
    ret.append(Course("10:00", "6", "سیستم عامل", "8:00", "محسن محسنی ", "1"))
    ret.append(Course("18:00", "7", "معماری کامپیوتر", "16:00", "علی محسنی ", "5"))
    ret.append(Course("14:00", "8", "تاریخ تحلیلی", "12:00", "سید محسن طباطبایی ", "1"))
    ret.append(Course("10:00", "9", "هوش مصنوعی", "8:00", "علی سلیمانی", "1"))
    ret.append(Course("15:00", "10", "ریزپردازنده", "12:00", "علی محسنی ", "5"))


    return ret

