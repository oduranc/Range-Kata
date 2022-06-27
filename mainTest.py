from unicodedata import name
import unittest
from main import Range

class mainTest(unittest.TestCase):
    
    def test_contains():
        r1 = Range('[2,6)')
        assert r1.contains('[2,4]') == True
    
if __name__ == '__main__':
    unittest.main()