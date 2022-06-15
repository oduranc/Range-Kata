
class LimitTypes:
    closeLimit = 'close'
    openLimit = 'open'

class Range:
    
    # Attributes:
    valueLeft = 0
    typeLeft = ''
    valueRight = 0
    typeRight = ''

    # Methods

    # Integer range contains
    def IntegerRangeContains(range1, numbers):
        i = 0
        flag = 0
        if range1.typeLeft == LimitTypes.closeLimit:
            if range1.typeRight == LimitTypes.closeLimit:
                for number in range(range1.valueLeft, range1.valueRight + 1):
                    if number != numbers[i]:
                        flag = flag + 1
                        i = i + 1
            else:
                range(range1.valueLeft, range1.valueRight)
        else:
            print()