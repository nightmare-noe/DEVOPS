import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        """
        Teste la méthode addition avec plusieurs cas.
        """
        self.assertEqual(SimpleMath.addition(2, 3), 5)
        self.assertEqual(SimpleMath.addition(0, 0), 0)
        self.assertEqual(SimpleMath.addition(-5, 5), 0)

    def test_soustraction(self):
        """
        Teste la méthode soustraction avec plusieurs cas.
        """
        self.assertEqual(SimpleMath.soustraction(5, 3), 2)
        self.assertEqual(SimpleMath.soustraction(0, 0), 0)
        self.assertEqual(SimpleMath.soustraction(-2, -3), 1)
