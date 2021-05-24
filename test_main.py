from unittest.case import TestCase

from main import hex_string_reverse, hex_part_reverse


class SnowrunnerTestCase(TestCase):
    def test_hex_string_reverse(self):
        self.assertEqual(hex_string_reverse('B1DC9D9F 96E1 7945 B3F1 4F 3D 51 71 B5 61'),
                         '9F9DDCB1E1964579F1B34F3D5171B561')

    def test_hex_part_reverse(self):
        self.assertEqual(hex_part_reverse('B1DC9D9F'), '9F9DDCB1')
        self.assertEqual(hex_part_reverse('96E1'), 'E196')
        self.assertEqual(hex_part_reverse('7945'), '4579')