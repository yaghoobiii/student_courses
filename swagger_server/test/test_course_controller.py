# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestCourseController(BaseTestCase):
    """CourseController integration test stubs"""

    def test_course_by_id(self):
        """Test case for course_by_id

        Get a specific course by ID
        """
        response = self.client.open(
            '/courses/{course_id}'.format(course_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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
