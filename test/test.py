import unittest
import tic_tac_toe

class Test_test(unittest.TestCase):
    def test_Mult(self):
        a=tic_tac_toe.Mult(0)
        self.assertEqual(a, 0)
        
        b=tic_tac_toe.Mult(-1)
        self.assertEqual(b, -3)

        c=tic_tac_toe.Mult(1)
        self.assertEqual(c, 3)
  

if __name__ == '__main__':
    unittest.main()
