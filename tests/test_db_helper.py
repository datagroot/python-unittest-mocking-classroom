from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDB(TestCase):
    def setUp(self):
        self.db = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, MockDB):
        db = MockDB()

        db.get_minimum_salary.return_value = 100
        db.get_maximum_salary.return_value = 5000

        actual_min_salary = db.get_minimum_salary()
        actual_max_salary = db.get_maximum_salary()

        self.assertGreater(actual_max_salary, actual_min_salary)