# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.course import Course  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCourseController(BaseTestCase):
    """CourseController integration test stubs"""

    def test_courses(self):
        """Test case for courses

        Get all the courses
        """
        response = self.client.open(
            '/courses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
