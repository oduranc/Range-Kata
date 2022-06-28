from unicodedata import name
import unittest
from src.Range_oduranc import Range

class mainTest(unittest.TestCase):
    
    # def test_contains():
    #     r1 = Range('[2,6)')
    #     assert r1.contains('[2,4]') == True

    def test_contains(self):
        r1 = Range('[2, 6)')
        self.assertTrue(r1.contains(2, 4))

        self.assertFalse(r1.contains(-1, 1, 6, 10))
        
    def test_getAllPoints(self):
        r1 = Range('[2, 6)')
        self.assertEqual(r1.getAllPoints(), [2, 3, 4, 5])
        
    def test_containsRange(self):
        r1 = Range('[2,5)')
        self.assertFalse(r1.containsRange('[7,10)'))
        
        self.assertFalse(r1.containsRange('[3,10)'))
        
        self.assertFalse(r1.containsRange('[2,10)'))
        
        self.assertFalse(r1.containsRange('[3,5]'))
        
        self.assertTrue(r1.containsRange('[3,5)'))

    def test_endPoints(self):
        r1 = Range('[2, 6)')
        r2 = Range('[2, 6]')
        r3 = Range('(2, 6)')
        r4 = Range('(2, 6]')

        self.assertEqual(r1.endPoints(), [2, 5])

        self.assertEqual(r2.endPoints(), [2, 6])

        self.assertEqual(r3.endPoints(), [3, 5])

        self.assertEqual(r4.endPoints(), [3, 6])

    def test_overlapsRange(self):
        r1 = Range('[2, 5)')
        
        paramRange = Range('[7, 10)')
        self.assertFalse(r1.overlapsRange(paramRange))
        self.assertTrue(r1.overlapsRange(Range('[3, 10)')))

        r2 = Range('[2, 10)')
        self.assertTrue(r2.overlapsRange(Range('[3, 5)')))

        r3 = Range('[3, 5)')
        self.assertTrue(r3.overlapsRange(r3))
        r4 = Range('[2, 10)')
        self.assertTrue(r3.overlapsRange(r4))

    def test_equals(self):
        r1 = Range('[3, 5)')
        r2 = Range('[2, 10)')
        r3 = Range('[2, 5)')
        r4 = Range('[3, 10)')

        self.assertTrue(r1.equals(r1))
        self.assertFalse(r3.equals(r4))
        self.assertFalse(r2.equals(r1))
        self.assertFalse(r1.equals(r2))
        
    
if __name__ == '__main__':
    unittest.main()