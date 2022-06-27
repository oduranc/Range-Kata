class Range:

    # Attributes
    newRange = ''

    # Constructor
    def __init__(self, newRange):
        self.newRange = newRange

    # Methods

    # Convert Range
    def ConvertRange(R1):
        if R1.newRange[0] == '[' and R1.newRange[-1] == ']':
            result = range(int(R1.newRange.split(',')[0][1:]), int(R1.newRange.split(',')[1][:-1]) + 1)
            return result

        elif R1.newRange[0] == '[' and R1.newRange[-1] == ')':
            result = range(int(R1.newRange.split(',')[0][1:]), int(R1.newRange.split(',')[1][:-1]))
            return result

        elif R1.newRange[0] == '(' and R1.newRange[-1] == ']':
            result = range(int(R1.newRange.split(',')[0][1:]) + 1, int(R1.newRange.split(',')[1][:-1]) + 1)
            return result

        elif R1.newRange[0] == '(' and R1.newRange[-1] == ')':
            result = range(int(R1.newRange.split(',')[0][1:]) + 1, int(R1.newRange.split(',')[1][:-1]))
            return result

    # Integer Range Contains
    def contains(R1, *numbers):
        convertedR1 = R1.ConvertRange()
        result = True
        for number in numbers:
            if number < convertedR1.start or number >= convertedR1.stop:
                result = False
                break
        return result
    
    # Get All Points
    def getAllPoints(R1):
        convertedR1 = R1.ConvertRange()
        allPoints = list(convertedR1)
        return allPoints
    
    # Contais Range
    def containsRange(R1, values):
        convertedR1 = R1.ConvertRange()
        R2 = Range(values)
        convertedR2 = R2.ConvertRange()
        if convertedR2.start < convertedR1.start or convertedR2.stop > convertedR1.stop:
            return False
        return True 

    # End Points
    def endPoints(R1):
        convertedR1 = R1.ConvertRange()
        result = [convertedR1.start, convertedR1.stop - 1]
        return result

    # Overlaps Range
    def overlapsRange(R1, R2):
        convertedR1 = R1.ConvertRange()
        convertedR2 = R2.ConvertRange()
        
        for num in convertedR2:
            if num < convertedR1.start or num >= convertedR1.stop:
                return False
        
        return True