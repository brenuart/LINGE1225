def plus_longue_periode_croissante01(data):

    sequenceSize = 0
    sequenceLastValue = 0
    maxSequenceSize = 0

    for value in data:
        if sequenceSize == 0 or value >= sequenceLastValue:
            sequenceSize += 1
            sequenceLastValue = value
        else:
            if sequenceSize > maxSequenceSize:
                maxSequenceSize = sequenceSize
            sequenceSize = 0

    if sequenceSize > maxSequenceSize:
        maxSequenceSize = sequenceSize

    return maxSequenceSize

# ----------------

data = [4150, 4250, 4300, 4300, 4200, 4200, 4300]
print(plus_longue_periode_croissante01(data))