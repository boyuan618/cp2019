import unittest
from product_code import *

class productCodeTest(unittest.TestCase):
    def testCode(self):
        self.assertEqual(product_code('A1234'), True)
        
        
if __name__ == "__main__":
    unittest.main()