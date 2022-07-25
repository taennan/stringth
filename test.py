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

    def test_from_nth_str_positive(self):
        """ """
        self.assertEqual(from_nth_str("1st"), 1)
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
