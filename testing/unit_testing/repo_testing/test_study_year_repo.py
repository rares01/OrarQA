import unittest
from unittest.mock import patch, MagicMock

from repositories.study_year_repo import get_study_years_values, get_id_by_value, get_value_by_id


class StudyYearRepoTesting(unittest.TestCase):
    def setUp(self):
        self.study_years = [1, 2, 3]
        self.mock_id = 1
        self.mock_wrong_id = 10000
        self.mock_study_year = 1
        self.mock_wrong_study_year = '8'

    @patch('repositories.study_year_repo.connection')
    def test_given_study_year_repo_when_get_study_year_values_then_returns_study_year_numbers(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,), (2,), (3,)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_study_years_values()

        self.assertEqual(result, self.study_years)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT number FROM studyyear")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    def test_given_get_id_by_value_when_study_year_is_correct_then_returns_study_year_id(self):
        result = get_id_by_value(self.mock_study_year)
        self.assertEqual(result, self.mock_id)

    def test_given_get_id_by_value_when_weekday_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_id_by_value(self.mock_wrong_study_year))

    def test_given_get_name_by_id_when_weekday_is_correct_then_returns_weekdays_name(self):
        result = get_value_by_id(self.mock_id)
        self.assertEqual(result, self.mock_study_year)

    def test_given_get_name_by_id_when_weekday_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_value_by_id(self.mock_wrong_id))

