# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.login_status import LoginStatus  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStudentController(BaseTestCase):
    """StudentController integration test stubs"""

    def test_login(self):
        """Test case for login

        Login interface for students
        """
        query_string = [('password', 'password_example')]
        response = self.client.open(
            '/login',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
