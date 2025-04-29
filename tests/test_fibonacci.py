import unittest
from src.fibonacci import fibonacci_iterative, fibonacci_recursive

class TestFibonacci(unittest.TestCase):

    def test_iterative_values(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(5), 5)
        self.assertEqual(fibonacci_iterative(10), 55)

    def test_recursive_values(self):
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(6), 8)
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-4)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-2)
