import unittest

from repositories.room_type_repo import get_room_type_values, get_id_by_value


class RoomTypeRepoTesting(unittest.TestCase):
    def setUp(self):
        self.room_types = ['Course', 'Laboratory', 'Seminary']
        self.mock_id = 1
        self.mock_wrong_id = 10000
        self.mock_room_type = 'Course'
        self.mock_wrong_room_type = 'Exam'

    def test_given_room_type_repo_when_get_room_type_values_then_returns_room_type_names(self):
        result = get_room_type_values()
        self.assertEqual(result, self.room_types)

    def test_given_get_id_by_value_when_semi_year_is_correct_then_returns_semi_year_id(self):
        result = get_id_by_value(self.mock_room_type)
        self.assertEqual(result, self.mock_id)

    def test_given_get_id_by_value_when_weekday_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_id_by_value(self.mock_wrong_room_type))


