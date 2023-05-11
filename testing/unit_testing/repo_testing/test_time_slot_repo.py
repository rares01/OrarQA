import unittest

from repositories.time_slot_repo import get_time_slot_values, get_id_by_value, get_timeslot_by_id


class TimeSlotRepoTesting(unittest.TestCase):
    def setUp(self):
        self.time_slots = ['8-10', '10-12', '12-14', '14-16', '16-18', '18-20']
        self.mock_id = 1
        self.mock_wrong_id = 10000
        self.mock_time_slot = '8:00-10:00'
        self.mock_start_hour = 8
        self.mock_end_hour = 10
        self.mock_wrong_end_hour = 24

    def test_given_time_slot_repo_when_get_time_slot_values_then_returns_time_slots(self):
        result = get_time_slot_values()
        self.assertEqual(result, self.time_slots)

    def test_given_get_id_by_value_when_time_slot_is_correct_then_returns_time_slot_id(self):
        result = get_id_by_value(self.mock_start_hour, self.mock_end_hour)
        self.assertEqual(result, self.mock_id)

    def test_given_get_id_by_value_when_time_slot_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_id_by_value(self.mock_start_hour, self.mock_wrong_end_hour))

    def test_given_get_name_by_id_when_time_slot_is_correct_then_returns_time_slot(self):
        result = get_timeslot_by_id(self.mock_id)
        self.assertEqual(result, self.mock_time_slot)

    def test_given_get_name_by_id_when_time_slot_is_wrong_then_throws_error(self):
        self.assertRaises(IndexError, get_timeslot_by_id(self.mock_wrong_id))

