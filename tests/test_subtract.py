import unittest
from subtract import subtracting

class TestSubtraction(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtracting(10, 5), 5)   # 10 - 5 = 5
        self.assertEqual(subtracting(20, 10), 10) # 20 - 10 = 10

    def test_subtract_with_negative_numbers(self):
        self.assertEqual(subtracting(-5, -3), -2) # -5 - (-3) = -2
        self.assertEqual(subtracting(-10, 5), -15) # -10 - 5 = -15

    def test_subtract_with_zero(self):
        self.assertEqual(subtracting(5, 0), 5)   # 5 - 0 = 5
        self.assertEqual(subtracting(0, 5), -5)  # 0 - 5 = -5

if __name__ == "__main__":
    unittest.main()
