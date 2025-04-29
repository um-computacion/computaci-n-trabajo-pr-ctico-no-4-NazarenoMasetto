import unittest
from src.flatten import flatten

class TestFlatten(unittest.TestCase):

    def test_lista_simple(self):
        self.assertEqual(flatten([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_lista_anidada(self):
        self.assertEqual(flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])

    def test_estructura_mixta(self):
        self.assertEqual(flatten([1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]),
                         [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8])
