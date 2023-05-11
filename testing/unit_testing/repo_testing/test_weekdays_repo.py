import unittest

from repositories.weekdays_repo import get_weekdays_values, get_id_by_value, get_name_by_id


class WeekdaysRepoTesting(unittest.TestCase):
    def setUp(self):
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.mock_id = 1
        self.mock_wrong_id = 10000
        self.mock_weekday = 'Monday'
        self.mock_wrong_weekday = 'Saturday'

    def test_given_weekdays_repo_when_get_weekdays_values_then_returns_weekdays_names(self):
        result = get_weekdays_values()
        self.assertEqual(result, self.weekdays)

    def test_given_get_id_by_value_when_weekday_is_correct_then_returns_weekdays_id(self):
        result = get_id_by_value(self.mock_weekday)
        self.assertEqual(result, self.mock_id)

    def test_given_get_id_by_value_when_weekday_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_id_by_value(self.mock_wrong_weekday))

    def test_given_get_name_by_id_when_weekday_is_correct_then_returns_weekdays_name(self):
        result = get_name_by_id(self.mock_id)
        self.assertEqual(result, self.mock_weekday)

    def test_given_get_name_by_id_when_weekday_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_name_by_id(self.mock_wrong_id))

