# coding: utf-8

from __future__ import absolute_import

from swagger_server.test import BaseTestCase


class TestSelectionController(BaseTestCase):
    """SelectionController integration test stubs"""

    def test_destroy_selection(self):
        """Test case for destroy_selection

        Destroy a selection
        """
        query_string = [('student', 56),
                        ('course', 56)]
        response = self.client.open(
            '/selections/destroy',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_selection(self):
        """Test case for insert_selection

        Create a selection
        """
        query_string = [('student', 56),
                        ('course', 56)]
        response = self.client.open(
            '/selections/create',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_selection_by_student(self):
        """Test case for selection_by_student

        Get a student's selections
        """
        response = self.client.open(
            '/selections/{student_id}'.format(student_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
