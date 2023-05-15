import unittest
from unittest.mock import MagicMock, patch

from repositories.student_repo import get_students, add_student, delete_student


def get_semiyear_id_side_effect(semiyear_id):
    if semiyear_id == 1:
        return "A"
    else:
        return "B"


def get_semiyear_name_side_effect(semiyear_name):
    if semiyear_name == "A":
        return 1
    else:
        return 2


def get_student_group_id_side_effect(student_group_id):
    if student_group_id == 1:
        return 101
    else:
        return 102


def get_student_group_name_side_effect(student_group_name):
    if student_group_name == 101:
        return 1
    else:
        return 2


def side_effect_error(id):
    raise IndexError("Index Error")


def study_year_method_side_effect(study_year_id):
    if study_year_id == 1:
        return 1
    else:
        return 2


def study_year_method_side_effect_2(study_year_value):
    if study_year_value == 1:
        return 1
    else:
        return 2


class StudentTesting(unittest.TestCase):
    @patch('repositories.student_repo.connection')
    @patch('repositories.student_repo.get_value_study_year')
    @patch('repositories.student_repo.get_value_semi_year')
    @patch('repositories.student_repo.get_value_student_group')
    def test_given_student_repo_when_get_students_then_successful(self, mock_student_group_method,
                                                                  mock_semi_year_method,
                                                                  mock_study_year_method,
                                                                  mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "John", "Smith", 1, 1, 1,)]
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_study_year_method.side_effect = study_year_method_side_effect
        mock_student_group_method.side_effect = get_student_group_id_side_effect
        mock_semi_year_method.side_effect = get_semiyear_id_side_effect

        result = get_students()

        self.assertEqual(1, result[0].id)
        self.assertEqual("John", result[0].first_name)
        self.assertEqual("Smith", result[0].last_name)
        self.assertEqual(1, result[0].study_year)
        self.assertEqual("A", result[0].semi_year)
        self.assertEqual(101, result[0].student_group)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM student")
        mock_cursor.close.assert_called_once()
        mock_student_group_method.assert_any_call(1)
        mock_semi_year_method.assert_any_call(1)
        mock_study_year_method.assert_any_call(1)

    @patch('repositories.student_repo.connection')
    @patch('repositories.student_repo.get_value_study_year')
    @patch('repositories.student_repo.get_value_semi_year')
    @patch('repositories.student_repo.get_value_student_group')
    def test_given_student_repo_when_get_students_with_bad_foreign_keys_then_throw_index_error(self,
                                                                                               mock_student_group_method,
                                                                                               mock_semi_year_method,
                                                                                               mock_study_year_method,
                                                                                               mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "John", "Smith", 1, 1, 1,)]
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_study_year_method.side_effect = study_year_method_side_effect
        mock_student_group_method.side_effect = side_effect_error
        mock_semi_year_method.side_effect = get_semiyear_id_side_effect

        self.assertRaises(IndexError, get_students)

        mock_conn.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_semi_year_method.assert_any_call(1)
        mock_study_year_method.assert_any_call(1)

    @patch('repositories.student_repo.connection')
    @patch('repositories.student_repo.get_id_study_year')
    @patch('repositories.student_repo.get_id_semi_year')
    @patch('repositories.student_repo.get_id_student_group')
    def test_given_student_repo_when_add_student_then_successful(self,
                                                                 mock_student_group_method,
                                                                 mock_semi_year_method,
                                                                 mock_study_year_method,
                                                                 mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_study_year_method.side_effect = study_year_method_side_effect_2
        mock_student_group_method.side_effect = get_student_group_name_side_effect
        mock_semi_year_method.side_effect = get_semiyear_name_side_effect

        add_student("John", "Smith", 1, "A", 101)

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO student (first_name, last_name, study_year_id, semi_year_id, student_group_id) VALUES (%s, %s,"
            " %s, %s, %s)",
            ("John", "Smith", "1", "1", "1"))
        mock_cursor.close.assert_called_once()
        mock_student_group_method.assert_any_call(101)
        mock_semi_year_method.assert_any_call("A")
        mock_study_year_method.assert_any_call(1)

    @patch('repositories.student_repo.connection')
    def test_given_student_repo_when_delete_student_then_successful(self,
                                                                    mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor

        delete_student(1)

        mock_conn.assert_called_once()
        mock_conn.return_value.commit.assert_called_once()
        mock_cursor.execute.assert_called_once_with("DELETE FROM student WHERE id=%s", (1,))
        mock_cursor.close.assert_called_once()
