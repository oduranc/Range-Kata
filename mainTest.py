from unittest import result
from main import LimitTypes, Range


import unittest

class RangeTest(unittest.TestCase):
    
    def With_Two_and_Four_Is_True(self):
        rangeObject = Range(2, LimitTypes.closeLimit, 6, LimitTypes.openLimit)
        result = rangeObject.IntegerRangeContains(rangeObject, [2, 4])
        self.assertTrue(result)
        
if __name__ == '__main__':
    unittest.main()