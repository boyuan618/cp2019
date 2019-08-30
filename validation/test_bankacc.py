
from bankacc import *
import unittest

class MyTestCase(unittest.TestCase):
    
    def setUp(self):
        self.bankacct = BankAccount("A01", 500)
    
    
    def test_deposit(self):
        self.assertEqual(self.bankacct.deposit(500), 1000)
        
    def test_withdraw(self):
        self.assertEqual(self.bankacct.withdraw(300), 200)
        
    def test_calc_interest(self):
        self.assertEqual(self.bankacct.calc_interest(10, 200), 243)

    def tearDown(self):
        self.bankacct = None
        
if __name__ == "__main__":
    unittest.main()
