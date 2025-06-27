import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        """
        Teste si la fonction addition retourne les bons résultats.
        """
        self.assertEqual(SimpleMath.addition(2, 3), 5)
        self.assertEqual(SimpleMath.addition(0, 0), 0)
        self.assertEqual(SimpleMath.addition(-5, 5), 0)
