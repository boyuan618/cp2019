from age_validation import *
import unittest

class AgeTest(unittest.TestCase):
    
    def test_age(self):
        self.assertEqual(ageCheck('100'), False)
        
        
if __name__ == "__main__":
    unittest.main()