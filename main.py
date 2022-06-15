
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
    
    def __init__(self, valueLeft, typeLeft, valueRight, typeRight):
        self.valueLeft = valueLeft
        self.typeLeft = typeLeft
        self.valueRight = valueRight
        self.typeRight = typeRight

    # Integer range contains
    def IntegerRangeContains(range1, numbertoCheck):
        if range1.typeLeft == LimitTypes.closeLimit:
            if range1.typeRight == LimitTypes.closeLimit:
                if numbertoCheck in range(range1.valueLeft, range1.valueRight + 1):
                    return True
                else:
                    return False
            else:
                if numbertoCheck in range(range1.valueLeft, range1.valueRight):
                    return True
                else:
                    return False
        else:
            if range1.typeRight == LimitTypes.closeLimit:
                if numbertoCheck in range(range1.valueLeft + 1, range1.valueRight + 1):
                    return True
                else:
                    return False
            else:
                if numbertoCheck in range(range1.valueLeft + 1, range1.valueRight):
                    return True
                else:
                    return False

    # Get All Points
    def GetAllPoints(range1):
        points = []
        if range1.typeLeft == LimitTypes.closeLimit:
            # Left Closed
            if range1.typeRight == LimitTypes.closeLimit:
                # Right Closed
                for number in range(range1.valueLeft, range1.valueRight + 1):
                    points.append(number)
            else:
                # Right Opened
                for number in range(range1.valueLeft, range1.valueRight):
                    points.append(number)
        else:
            # Left Opened
            if range1.typeRight == LimitTypes.closeLimit:
                # Right Closed
                for number in range(range1.valueLeft + 1, range1.valueRight + 1):
                    points.append(number)
            else:
                # Right Opened
                for number in range(range1.valueLeft + 1, range1.valueRight):
                    points.append(number)
        return points