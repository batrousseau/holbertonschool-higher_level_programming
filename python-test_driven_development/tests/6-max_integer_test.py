#!/usr/bin/python3

import unittest
max_integer = __import__("6-max_integer").max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """
    A proper coded function should have passed this kind of test
    def test_type_parameter_check(self):
        self.assertRaises(TypeError, max_integer, "I'm a string")
        self.assertRaises(TypeError, max_integer, 42)
        self.assertRaises(TypeError, max_integer, True)
        this_dict: dict = {"example" : 42}
        self.assertRaises(TypeError, max_integer, this_dict)
        this_tuple: tuple = (1, 2, 3, 4)
        self.assertRaises(TypeError, max_integer, this_tuple)"""

    def test_empty_list_check(self):
        empty_list: list = ()
        self.assertIsNone(max_integer(empty_list))

    def test_not_int_list_check(self):
        weird_list: list = (1, "c", True, 3, )
        self.assertRaises(TypeError, max_integer, weird_list)

    def test_normal_behaviour_check(self):
        classic_list: list = (1, 542, -4, 12000, 5, 63, 48, 2, 98)
        result = 12000
        self.assertTrue(max_integer(classic_list), result)


if __name__ == "__main__":
    unittest.main()
