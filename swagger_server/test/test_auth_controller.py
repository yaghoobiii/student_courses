# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_login(self):
        """Test case for login

        Login interface for students
        """
        query_string = [('user_id', 111),
                        ('password', 'password_example')]
        response = self.client.open(
            '/login',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
