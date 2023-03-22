"""simple test
"""

from django.test import SimpleTestCase

from app.calc import add, sub


class CalTests(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """test adding numbers together"""
        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """test subtracting numbers"""
        res = sub(10, 5)
        self.assertEqual(res, 5)
