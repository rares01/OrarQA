import unittest
from unittest.mock import patch, MagicMock

from repositories.room_repo import get_room_values, get_rooms_by_room_type, get_id_by_value, get_value_by_id


def room_type_method_side_effect(room_type):
    if room_type == 'Course':
        return 1
    elif room_type == 'Laboratory':
        return 2
    else:
        return 3


def side_effect_error(id):
    raise IndexError("Index Error")


class RoomTesting(unittest.TestCase):
    @patch('repositories.room_repo.connection')
    def test_given_room_repo_when_get_room_values_then_returns_correctly(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("A101", "Course"), ("B203", "Laboratory")]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_room_values()

        self.assertEqual(len(result), 2)
        self.assertEqual("A101", result[0])
        self.assertEqual("B203", result[1])
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT name FROM room")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.room_repo.connection')
    @patch('repositories.room_repo.get_id_by_value')
    def test_given_room_repo_when_get_rooms_by_room_type_then_returns_correctly(self, mock_room_type_method, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("A101", "Course")]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_room_type_method.side_effect = room_type_method_side_effect

        result = get_rooms_by_room_type("Course")

        self.assertEqual(["A101"], result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT name FROM room WHERE room_type_id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_room_type_method.assert_any_call('Course')
        mock_cursor.close.assert_called_once()

    @patch('repositories.room_repo.connection')
    @patch('repositories.room_repo.get_id_by_value')
    def test_given_room_repo_when_get_rooms_by_room_type_then_returns_correctly(self, mock_room_type_method, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("A101", "Course")]
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_room_type_method.side_effect = side_effect_error

        with self.assertRaises(IndexError):
            get_rooms_by_room_type("Course")

    @patch('repositories.room_repo.connection')
    def test_given_room_repo_when_get_id_by_value_then_returns_correctly(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_id_by_value("A101")

        self.assertEqual(1, result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM room WHERE name=%s", ("A101",))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.room_repo.connection')
    def test_given_room_repo_when_get_value_by_id_then_returns_correctly(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("A101",)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_value_by_id(1)

        self.assertEqual("A101", result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT name FROM room WHERE id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
