import unittest
from problem1 import find_first_num, find_last_num, give_value_first, give_value_second

class TestFunctions(unittest.TestCase):

    def test_find_first_num(self):
        self.assertEqual(find_first_num("abc123def", 0), 123)
        # Add more test cases for find_first_num function

    def test_find_last_num(self):
        self.assertEqual(find_last_num("abc123def", 0), 123)
        # Add more test cases for find_last_num function

    def test_give_value_first(self):
        self.assertEqual(give_value_first(100, 50), 10050)
        # Add more test cases for give_value_first function

    def test_give_value_second(self):
        self.assertEqual(give_value_second(50, 100), 50100)
        # Add more test cases for give_value_second function

if __name__ == '__main__':
    unittest.main()
