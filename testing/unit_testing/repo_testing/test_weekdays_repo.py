import unittest
from unittest.mock import MagicMock, patch

from repositories.weekdays_repo import get_weekdays_values, get_id_by_value, get_name_by_id


class WeekdaysRepoTesting(unittest.TestCase):
    def setUp(self):
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday']
        self.mock_id = 1
        self.mock_wrong_id = 10000
        self.mock_weekday = 'Monday'
        self.mock_wrong_weekday = 'Saturday'

    @patch('repositories.weekdays_repo.connection')
    def test_given_study_year_repo_when_get_study_year_values_then_returns_study_year_numbers(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('Monday',), ('Tuesday',), ('Wednesday',)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_weekdays_values()

        self.assertEqual(self.weekdays, result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT day FROM weekday")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.weekdays_repo.connection')
    def test_given_weekdays_repo_when_get_name_by_id_then_returns_weekday_name(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(2, 'Monday')]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_name_by_id(2)

        self.assertEqual('Monday', result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM weekday WHERE id=%s", (2,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.weekdays_repo.connection')
    def test_given_weekdays_repo_when_get_id_by_value_then_returns_weekday_id(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(2,)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_id_by_value('Monday')
        self.assertEqual(result, 2)

        mock_cursor.execute.assert_called_once_with("SELECT id FROM weekday WHERE day=%s", ('Monday',))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

        mock_conn.assert_called_once()
        mock_conn.return_value.close.assert_called_once()

    @patch('repositories.weekdays_repo.connection')
    def test_given_weekdays_repo_when_get_id_by_value_with_nonexistent_name_then_raises_error(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_conn.return_value.cursor.return_value = mock_cursor

        with self.assertRaises(IndexError):
            get_id_by_value('Friday')

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM weekday WHERE day=%s", ('Friday',))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
