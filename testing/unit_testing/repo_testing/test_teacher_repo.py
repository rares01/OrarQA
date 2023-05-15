import unittest
from unittest.mock import MagicMock, patch

from entities.teacher import Teacher
from repositories.teacher_repo import get_teacher_full_names, get_teachers, get_full_teachers, add_teacher, \
    get_teacher_id_by_full_name, get_teacher_full_name_by_id


class TestTeacherRepo(unittest.TestCase):
    @patch('repositories.teacher_repo.connection')
    def test_given_teacher_repo_when_get_teacher_full_name_by_id_then_returns_full_name(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('John', 'Smau')]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_teacher_full_name_by_id(1)

        self.assertEqual(result, 'John Smau')

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT first_name, last_name FROM teacher where id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.teacher_repo.connection')
    def test_given_teacher_repo_when_get_teacher_full_names_then_returns_teacher_full_names(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('John', 'Doe'), ('Jane', 'Doe')]
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_teacher_full_names()

        self.assertEqual(result, ['John Doe', 'Jane Doe'])
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT first_name, last_name FROM teacher")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.teacher_repo.connection')
    def test_given_teacher_repo_when_get_teacher_id_by_full_name_with_valid_input_then_returns_id(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        mock_conn.return_value.cursor.return_value = mock_cursor

        expected_result = 1
        result = get_teacher_id_by_full_name("John Smau")

        self.assertEqual(result, expected_result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM teacher WHERE first_name=%s AND last_name=%s",
                                                    ("John", "Smau",))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.teacher_repo.connection')
    def test_given_teacher_repo_when_add_teacher_with_valid_input_then_adds_teacher(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor

        first_name = "John"
        last_name = "Smau"
        add_teacher(first_name, last_name)

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO teacher (first_name, last_name) VALUES (%s,%s)", (first_name, last_name))
        mock_conn.return_value.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.return_value.close.assert_called_once()

    @patch('repositories.teacher_repo.connection')
    def test_given_teacher_repo_when_get_full_teachers_then_returns_list_of_teacher_objects(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'John', 'Doe'), (2, 'Jane', 'Doe')]
        mock_conn.return_value.cursor.return_value = mock_cursor

        teachers = get_full_teachers()

        self.assertEqual(len(teachers), 2)
        self.assertIsInstance(teachers[0], Teacher)
        self.assertEqual(teachers[0].first_name, 'John')
        self.assertEqual(teachers[0].last_name, 'Doe')
        self.assertEqual(teachers[0].id, 1)

        self.assertIsInstance(teachers[1], Teacher)
        self.assertEqual(teachers[1].first_name, 'Jane')
        self.assertEqual(teachers[1].last_name, 'Doe')
        self.assertEqual(teachers[1].id, 2)

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM teacher")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.teacher_repo.connection')
    def test_given_teacher_repo_when_get_teachers_with_valid_input_then_returns_teachers(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'John', 'Doe'), (2, 'Jane', 'Doe')]
        mock_conn.return_value.cursor.return_value = mock_cursor

        teachers = get_teachers()

        self.assertEqual(len(teachers), 2)
        self.assertIsInstance(teachers[0], Teacher)
        self.assertEqual(teachers[0].first_name, 'John')
        self.assertEqual(teachers[0].last_name, 'Doe')
        self.assertEqual(teachers[0].id, 1)

        self.assertIsInstance(teachers[1], Teacher)
        self.assertEqual(teachers[1].first_name, 'Jane')
        self.assertEqual(teachers[1].last_name, 'Doe')
        self.assertEqual(teachers[1].id, 2)

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT first_name, last_name FROM teacher")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()