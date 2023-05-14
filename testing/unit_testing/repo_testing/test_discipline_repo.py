import unittest
from unittest.mock import patch, MagicMock

from entities.discipline import Discipline
from repositories.discipline_repo import get_disciplines


def teacher_method_side_effect(teacher_id):
    if teacher_id == 1:
        return 'John Smith'
    else:
        return 'Alice Smith'


class DisciplineTesting(unittest.TestCase):
    def setUp(self):
        self.expected_disciplines = [Discipline(1, "SD", 1, "John Smith"), Discipline(2, "IP", 2, "Alice Smith")]

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.discipline_repo.get_teacher_full_name_by_id')
    def test_given_discipline_repo_when_get_disciplines_then_returns_correctly(self, mock_teacher_method, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, "SD", 1, 1), (2, "IP", 2, 2)]
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect

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
