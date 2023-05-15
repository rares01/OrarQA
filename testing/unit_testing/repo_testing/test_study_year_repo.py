import unittest
from unittest.mock import patch, MagicMock

from repositories.study_year_repo import get_study_years_values, get_id_by_value


class StudyYearRepoTesting(unittest.TestCase):
    def setUp(self):
        self.study_years = [1, 2, 3]

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

    @patch('repositories.study_year_repo.connection')
    def test_given_study_year_repo_when_get_id_by_value_with_valid_input_then_returns_id(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_id_by_value(1)

        self.assertEqual(result, 1)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM studyyear WHERE number=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.study_year_repo.connection')
    def test_given_study_year_repo_when_get_id_by_value_with_valid_input_then_returns_id(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_id_by_value(1)

        self.assertEqual(result, 1)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM studyyear WHERE number=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
