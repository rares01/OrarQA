import unittest
from unittest.mock import patch, MagicMock, PropertyMock

from entities.discipline import Discipline
from repositories.discipline_repo import get_disciplines, get_disciplines_value, add_discipline, delete_discipline, \
    get_discipline_id_by_value, get_discipline_by_id


def teacher_method_side_effect(teacher_id):
    if teacher_id == 1:
        return 'John Smith'
    else:
        return 'Alice Smith'


def teacher_method_side_effect_2(teacher_value):
    if teacher_value == 'John Smith':
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


class DisciplineTesting(unittest.TestCase):
    def setUp(self):
        self.expected_disciplines = [Discipline(1, "SD", 1, "John Smith"), Discipline(2, "IP", 2, "Alice Smith")]

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.discipline_repo.get_teacher_full_name_by_id')
    @patch('repositories.discipline_repo.get_value_by_id')
    def test_given_discipline_repo_when_get_disciplines_then_returns_correctly(self, mock_study_year_method,
                                                                               mock_teacher_method, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "SD", 1, 1), (2, "IP", 2, 2)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect
        mock_study_year_method.side_effect = study_year_method_side_effect

        result = get_disciplines()

        self.assertEqual(len(result), 2)
        self.assertEqual(self.expected_disciplines[0].id, result[0].id)
        self.assertEqual(self.expected_disciplines[1].id, result[1].id)
        self.assertEqual(self.expected_disciplines[0].name, result[0].name)
        self.assertEqual(self.expected_disciplines[1].name, result[1].name)
        self.assertEqual(self.expected_disciplines[0].study_year, result[0].study_year)
        self.assertEqual(self.expected_disciplines[1].study_year, result[1].study_year)
        self.assertEqual(self.expected_disciplines[0].teacher_full_name, result[0].teacher_full_name)
        self.assertEqual(self.expected_disciplines[1].teacher_full_name, result[1].teacher_full_name)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM discipline")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_teacher_method.assert_any_call(1)
        mock_teacher_method.assert_any_call(2)
        mock_study_year_method.assert_any_call(1)
        mock_study_year_method.assert_any_call(2)

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.discipline_repo.get_teacher_full_name_by_id')
    @patch('repositories.discipline_repo.get_value_by_id')
    def test_given_discipline_repo_when_get_disciplines_get_teacher_fail_then_throws_index_error(self,
                                                                                                 mock_study_year_method,
                                                                                                 mock_teacher_method,
                                                                                                 mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "SD", 1, 1), (2, "IP", 2, 2)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = side_effect_error
        mock_study_year_method.side_effect = study_year_method_side_effect

        self.assertRaises(IndexError, get_disciplines)

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.discipline_repo.get_teacher_full_name_by_id')
    @patch('repositories.discipline_repo.get_value_by_id')
    def test_given_discipline_repo_when_get_disciplines_get_study_year_fail_then_throws_index_error(self,
                                                                                                    mock_study_year_method,
                                                                                                    mock_teacher_method,
                                                                                                    mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "SD", 1, 1), (2, "IP", 2, 2)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect
        mock_study_year_method.side_effect = side_effect_error

        self.assertRaises(IndexError, get_disciplines)
        mock_teacher_method.assert_any_call(1)

    @patch('repositories.discipline_repo.connection')
    def test_given_discipline_repo_when_get_disciplines_value_then_returns_correctly(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "SD", 1, 1), (2, "IP", 2, 2)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_disciplines_value()

        self.assertEqual(len(result), 2)
        self.assertEqual("SD", result[0])
        self.assertEqual("IP", result[1])
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM discipline")
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.discipline_repo.get_teacher_id_by_full_name')
    @patch('repositories.discipline_repo.get_id_by_value')
    def test_given_discipline_repo_when_add_disciplines_then_successful(self, mock_study_year_method,
                                                                        mock_teacher_method, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect_2
        mock_study_year_method.side_effect = study_year_method_side_effect_2
        mock_conn.return_value.closed = 1

        add_discipline('SD', 1, 'John Smith')

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO discipline (name, study_year_id, teacher_id) VALUES (%s,%s,%s)",
            ('SD', 1, 1,))
        mock_cursor.close.assert_called_once()
        mock_teacher_method.assert_any_call("John Smith")
        mock_study_year_method.assert_any_call(1)

    @patch('repositories.discipline_repo.connection')
    def test_given_discipline_repo_when_remove_disciplines_then_successful(self, mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_conn.return_value.closed = 1

        delete_discipline(1)

        mock_cursor.execute.assert_called_once_with(
            "DELETE FROM discipline WHERE id=%s", (1,)
        )
        mock_conn.return_value.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_conn.return_value.close.assert_called_once()

    @patch('repositories.discipline_repo.connection')
    def test_given_discipline_repo_when_get_disciplines_id_by_value_then_returns_correctly(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "SD", 1, 1), (2, "IP", 2, 2)]
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_conn.return_value.closed = 1

        result = get_discipline_id_by_value("SD")

        self.assertEqual(1, result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT id FROM discipline WHERE name=%s", ("SD",))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.discipline_repo.connection')
    def test_given_discipline_repo_when_get_disciplines_by_id_then_returns_correctly(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "SD", 1, 1), (2, "IP", 2, 2)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_discipline_by_id(1)

        self.assertEqual("SD", result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with("SELECT * FROM discipline WHERE id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
