from unittest.case import TestCase

from main import hex_string_reverse


class SnowrunnerTestCase(TestCase):
    def test_hex_string_reverse(self):
        self.assertEqual(hex_string_reverse('B1DC9D9F 96E1 7945 B3F1 4F 3D 51 71 B5 61'),
                         '9F9DDCB1 E196 4579 F1B3 4F 3D 51 71 B5 61')
