class Range:
    
    # Attributes
    newRange = ''

    # Constructor
    def __init__(self, newRange):
        self.newRange = newRange

    # Methods

    #
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