import unittest
from src.factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):

    def test_iterative_positive(self):
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(0), 1)

    def test_recursive_positive(self):
        self.assertEqual(factorial_recursive(4), 24)
        self.assertEqual(factorial_recursive(1), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(-3)

