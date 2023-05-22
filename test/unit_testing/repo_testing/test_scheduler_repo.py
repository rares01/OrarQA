import unittest
from unittest.mock import patch, MagicMock

from repositories.scheduler_repo import add_entry


class TestSchedulerRepo(unittest.TestCase):

    @patch('repositories.scheduler_repo.connection')
    def test_given_scheduler_repo_when_add_entry_with_valid_input_then_adds_entry(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_conn.return_value.closed = 1

        id = 1
        add_entry(id)

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO scheduler (id) VALUES (%s)", (id,))
        mock_conn.return_value.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.return_value.close.assert_called_once()
