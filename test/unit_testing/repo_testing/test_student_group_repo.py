from unittest import TestCase
from unittest.mock import MagicMock, patch

from entities.student_group import StudentGroup
from repositories.student_group_repo import get_student_groups, get_student_groups_values, get_id_by_value, \
    get_value_by_id


class TestTimeslotRepo(TestCase):
    @patch('repositories.student_group_repo.connection')
    def test_get_student_groups(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 1), (2, 2)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_student_groups()

        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], StudentGroup)
        self.assertEqual(result[0].id, 1)
        self.assertEqual(result[0].number, 1)

        self.assertIsInstance(result[1], StudentGroup)
        self.assertEqual(result[1].id, 2)
        self.assertEqual(result[1].number, 2)

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with('SELECT * FROM studentgroup')
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.student_group_repo.connection')
    def test_given_timeslot_repo_when_get_student_groups_values_then_returns_list_of_group_numbers(self, mock_conn):
        # Arrange
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,), (2,), (3,)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = [1, 2, 3]

        # Act
        result = get_student_groups_values()

        # Assert
        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT number FROM studentgroup")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.student_group_repo.connection')
    def test_given_student_group_repo_when_get_id_by_value_with_valid_input_then_returns_id(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "1")]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = 1
        result = get_id_by_value("1")

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM studentgroup WHERE number=%s", ("1",))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.student_group_repo.connection')
    def test_given_student_group_repo_when_get_value_by_id_with_valid_input_then_returns_number(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("1",)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = "1"
        result = get_value_by_id(1)

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT number FROM studentgroup WHERE id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
