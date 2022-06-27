from unicodedata import name
import unittest
from main import Range

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
        
        self.assertTrue(r1.containsRange('[3,5]'))
        
        self.assertTrue(r1.containsRange('[3,5)'))
        
    
if __name__ == '__main__':
    unittest.main()