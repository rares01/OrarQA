import unittest

from repositories.semi_year_repo import get_semi_years_values, get_id_by_value, get_value_by_id


class StudyYearRepoTesting(unittest.TestCase):
    def setUp(self):
        self.semi_years = ['A', 'B', 'E']
        self.mock_id = 1
        self.mock_wrong_id = 10000
        self.mock_semi_year = 'A'
        self.mock_wrong_semi_year = 'C'

    def test_given_semi_year_repo_when_get_semi_year_values_then_returns_semi_year_names(self):
        result = get_semi_years_values()
        self.assertEqual(result, self.semi_years)

    def test_given_get_id_by_value_when_semi_year_is_correct_then_returns_semi_year_id(self):
        result = get_id_by_value(self.mock_semi_year)
        self.assertEqual(result, self.mock_id)

    def test_given_get_id_by_value_when_weekday_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_id_by_value(self.mock_wrong_semi_year))

    def test_given_get_name_by_id_when_weekday_is_correct_then_returns_weekdays_name(self):
        result = get_value_by_id(self.mock_id)
        self.assertEqual(result, self.mock_semi_year)

    def test_given_get_name_by_id_when_weekday_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_value_by_id(self.mock_wrong_id))

