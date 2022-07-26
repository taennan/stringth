from stringth import to_nth_str, from_nth_str
from unittest import TestCase

class _TestModuleFuncs(TestCase):
    """ """

    def test_to_nth_str(self):
        """ """
        self.assertEqual(to_nth_str(1), "1st")
        self.assertEqual(to_nth_str(2), "2nd")
        self.assertEqual(to_nth_str(3), "3rd")

        self.assertEqual(to_nth_str(10), "10th")
        self.assertEqual(to_nth_str(-8), "-8th")

    def test_to_nth_str_11_12_13(self):
        """ """
        self.assertEqual(to_nth_str(11), "11th")
        self.assertEqual(to_nth_str(12), "12th")
        self.assertEqual(to_nth_str(13), "13th")

    def test_to_nth_str_x1st_x2nd_x3rd(self):
        """ """
        self.assertEqual(to_nth_str(21),     "21st")
        self.assertEqual(to_nth_str(652),    "652nd")
        self.assertEqual(to_nth_str(10_003), "10003rd")

    def test_from_nth_str_positive(self):
        """ """
        self.assertEqual(from_nth_str("1st"),  1)
        self.assertEqual(from_nth_str(" 2nd"), 2)
        self.assertEqual(from_nth_str("3rd "), 3)

        self.assertEqual(from_nth_str(" 11th "), 11)

    def test_from_nth_str_negative(self):
        """ """
        self.assertEqual(from_nth_str("-14th"),  -14)
        self.assertEqual(from_nth_str("-101th"), -101)

    def test_from_nth_str_fails(self):
        """ """
        self.assertEqual(from_nth_str("w1st"), None)
        self.assertEqual(from_nth_str("2ndd"), None)
        self.assertEqual(from_nth_str("3rrd"), None)
