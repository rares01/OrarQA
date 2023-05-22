import unittest
from unittest.mock import MagicMock, patch

from repositories.semi_year_repo import get_semi_years_values, get_id_by_value, get_value_by_id


class StudyYearRepoTesting(unittest.TestCase):
    @patch('repositories.semi_year_repo.connection')
    def test_given_timeslot_repo_when_get_semi_years_values_then_returns_semi_years(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("Spring 2022",), ("Fall 2022",)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = ["Spring 2022", "Fall 2022"]
        result = get_semi_years_values()

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT name FROM semiyear")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.semi_year_repo.connection')
    def test_given_semiyear_repo_when_get_id_by_value_with_valid_input_then_returns_id(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "A")]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = 1
        result = get_id_by_value("A")

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM semiyear WHERE name=%s", ("A",))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.semi_year_repo.connection')
    def test_given_semester_repo_when_get_value_by_id_with_valid_input_then_returns_value(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('A',)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = 'A'
        result = get_value_by_id(1)

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT name FROM semiyear WHERE id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
