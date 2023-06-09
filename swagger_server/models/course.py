# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from swagger_server import util
from swagger_server.models.base_model_ import Model


class Course(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int = None, name: str = None, teacher_name: str = None, weak_day: int = None,
                 start_time: str = None, end_time: str = None):  # noqa: E501
        """Course - a model defined in Swagger

        :param id: The id of this Course.  # noqa: E501
        :type id: int
        :param name: The name of this Course.  # noqa: E501
        :type name: str
        :param teacher_name: The teacher_name of this Course.  # noqa: E501
        :type teacher_name: str
        :param weak_day: The weak_day of this Course.  # noqa: E501
        :type weak_day: int
        :param start_time: The start_time of this Course.  # noqa: E501
        :type start_time: str
        :param end_time: The end_time of this Course.  # noqa: E501
        :type end_time: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'teacher_name': str,
            'weak_day': int,
            'start_time': str,
            'end_time': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'teacher_name': 'teacher_name',
            'weak_day': 'weak_day',
            'start_time': 'start_time',
            'end_time': 'end_time'
        }
        self._id = id
        self._name = name
        self._teacher_name = teacher_name
        self._weak_day = weak_day
        self._start_time = start_time
        self._end_time = end_time

    @classmethod
    def from_dict(cls, dikt) -> 'Course':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Course of this Course.  # noqa: E501
        :rtype: Course
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Course.


        :return: The id of this Course.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Course.


        :param id: The id of this Course.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Course.


        :return: The name of this Course.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Course.


        :param name: The name of this Course.
        :type name: str
        """

        self._name = name

    @property
    def teacher_name(self) -> str:
        """Gets the teacher_name of this Course.


        :return: The teacher_name of this Course.
        :rtype: str
        """
        return self._teacher_name

    @teacher_name.setter
    def teacher_name(self, teacher_name: str):
        """Sets the teacher_name of this Course.


        :param teacher_name: The teacher_name of this Course.
        :type teacher_name: str
        """

        self._teacher_name = teacher_name

    @property
    def weak_day(self) -> int:
        """Gets the weak_day of this Course.


        :return: The weak_day of this Course.
        :rtype: int
        """
        return self._weak_day

    @weak_day.setter
    def weak_day(self, weak_day: int):
        """Sets the weak_day of this Course.


        :param weak_day: The weak_day of this Course.
        :type weak_day: int
        """

        self._weak_day = weak_day

    @property
    def start_time(self) -> str:
        """Gets the start_time of this Course.


        :return: The start_time of this Course.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: str):
        """Sets the start_time of this Course.


        :param start_time: The start_time of this Course.
        :type start_time: str
        """

        self._start_time = start_time

    @property
    def end_time(self) -> str:
        """Gets the end_time of this Course.


        :return: The end_time of this Course.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: str):
        """Sets the end_time of this Course.


        :param end_time: The end_time of this Course.
        :type end_time: str
        """

        self._end_time = end_time
