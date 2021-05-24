from unittest.case import TestCase

from main import hex_string_reverse, hex_part_reverse, filename_parser


class SnowrunnerTestCase(TestCase):
    def test_hex_string_reverse(self):
        self.assertEqual(hex_string_reverse('B1DC9D9F 96E1 7945 B3F1 4F 3D 51 71 B5 61'),
                         '9F9DDCB1E1964579F1B34F3D5171B561')

    def test_hex_part_reverse(self):
        self.assertEqual(hex_part_reverse('B1DC9D9F'), '9F9DDCB1')
        self.assertEqual(hex_part_reverse('96E1'), 'E196')
        self.assertEqual(hex_part_reverse('7945'), '4579')

    def test_filename_parser(self):
        self.assertEqual(filename_parser('''43006F006D0070006C006500740065005300610076006500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004D20A19BF0F4D44A03B6BC8E7CC248504D20A19BF0F4D44A03B6BC8E7CC2485'''),
                         {'CompleteSave': '190AD2040FBF444D3BA06BC8E7CC2485'})


