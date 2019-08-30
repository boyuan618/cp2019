from calculator import *
import unittest

class MyTestCases(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        
    def test_subtract(self):
        self.assertEqual(subtract(6, 5), 1)
        
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        
    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        
    def test_dec2bin(self):
        self.assertEqual(dec2bin(34), '100010')
        
if __name__ == "__main__":
    unittest.main()
        