import unittest
from unittest.mock import patch, MagicMock

from repositories.time_slot_repo import get_time_slot_values, get_id_by_value, get_timeslot_by_id


class TimeSlotRepoTesting(unittest.TestCase):

    @patch('repositories.time_slot_repo.connection')
    def test_given_teacher_repo_when_get_time_slot_values_then_returns_values(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, '09:00', '10:30'), (2, '11:00', '12:30')]
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = ['09:00-10:30', '11:00-12:30']
        result = get_time_slot_values()

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM timeslot")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.time_slot_repo.connection')
    def test_get_id_by_value(self, mock_conn):
        # Arrange
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        # Act
        result = get_id_by_value("09:00", "10:00")

        # Assert
        self.assertEqual(result, 1)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "SELECT id FROM timeslot WHERE start_hour=%s AND end_hour=%s",
            ("09:00", "10:00")
        )
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.time_slot_repo.connection')
    def test_given_timeslot_repo_when_get_timeslot_by_id_with_valid_input_then_returns_timeslot(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "09:00", "10:00")]
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = "09:00:00-10:00:00"
        result = get_timeslot_by_id(1)

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM timeslot WHERE id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
