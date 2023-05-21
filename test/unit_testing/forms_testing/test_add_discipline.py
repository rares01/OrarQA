import tkinter as tk
import unittest
from unittest.mock import Mock, patch, MagicMock, call

import ui.admin.views.disciplines_view as view


class TestAddDisciplineForm(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    @patch('repositories.discipline_repo.connection')
    def test_handle(self, mock_conn_disciplines):
        form = view.AddDisciplineForm(self.root)

        name = "SD"
        year = 1
        teacher = "John Doe"

        disciplines = [
            (10, "TW", 1, 1),
            (11, "BD", 1, 1),
            (12, "SD", 1, 1)
        ]

        mock_cursor_disciplines = MagicMock()
        mock_cursor_disciplines.fetchall.return_value = disciplines
        mock_conn_disciplines.return_value.cursor.return_value = mock_cursor_disciplines
        mock_conn_disciplines.return_value.closed = 1

        form.handle(name_entry=tk.StringVar(value=name), year_entry=tk.StringVar(value=str(year)),
                    teacher_entry=tk.StringVar(value=teacher))

        expected_calls = [
            call('INSERT INTO discipline (name, study_year_id, teacher_id) VALUES (%s,%s,%s)', ('SD', 1, 2)),
            call('SELECT * FROM discipline')
        ]

        mock_cursor_disciplines.execute.assert_has_calls(expected_calls)

    @patch('repositories.discipline_repo.connection')
    def test_fetch_added_discipline(self, mock_conn_disciplines):
        form = view.AddDisciplineForm(self.root)

        mock_master = Mock()
        form.master = mock_master

        expected_disciplines = [
            (10, "TW", 1, 1),
            (11, "BD", 1, 1),
            (12, "SD", 1, 1)
        ]

        mock_cursor_disciplines = MagicMock()
        mock_cursor_disciplines.fetchall.return_value = expected_disciplines
        mock_conn_disciplines.return_value.cursor.return_value = mock_cursor_disciplines
        mock_conn_disciplines.return_value.closed = 1
        form.disciplines_view = view.DisciplinesView(self.root)
        form.disciplines_view.set_disciplines(expected_disciplines)

        form.go_back()

        current_frame = self.root.winfo_children()[-1]

        self.assertIsInstance(current_frame, view.DisciplinesView)

        updated_disciplines = form.disciplines_view.disciplines
        self.assertEqual(len(updated_disciplines), len(expected_disciplines))
        for index in range(len(updated_disciplines)):
            self.assertEqual(updated_disciplines[index].name, expected_disciplines[index][1])
