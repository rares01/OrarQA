import unittest
from unittest.mock import patch, MagicMock

from repositories.room_type_repo import get_room_type_values, get_id_by_value


class RoomTypeRepoTesting(unittest.TestCase):
    @patch('repositories.room_type_repo.connection')
    def test_given_room_type_repo_when_get_room_type_values_then_returns_room_type_names(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("Course",), ("Laboratory",), ("Seminary",)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_room_type_values()

        self.assertEqual(len(result), 3)
        self.assertEqual("Course", result[0])
        self.assertEqual("Laboratory", result[1])
        self.assertEqual("Seminary", result[2])
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT name FROM roomtype")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.room_type_repo.connection')
    def test_given_room_type_repo_when_get_id_by_value_then_returns_room_type_names(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_id_by_value("Course")

        self.assertEqual(1, result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM roomtype WHERE name=%s", ("Course",))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
