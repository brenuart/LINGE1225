def plus_longue_periode_croissante01(data):

    maxSequenceSize = 0
    sequenceSize = 0
    lastValue = 0

    for value in data:
        if sequenceSize == 0 or value > lastValue:
            sequenceSize += 1
            lastValue = value
        else:
            if sequenceSize > maxSequenceSize:
                maxSequenceSize = sequenceSize
            sequenceSize = 1

    if sequenceSize > maxSequenceSize:
        maxSequenceSize = sequenceSize

    return maxSequenceSize

# ----------------

data = [4150, 4250, 4300, 4300, 4200, 4200, 4300]
print(plus_longue_periode_croissante01(data)) # 3

data = [1, 2, 0, 3, 4, 5]
print(plus_longue_periode_croissante01(data)) # 4

data = []
print(plus_longue_periode_croissante01(data)) # 0

data = [1]
print(plus_longue_periode_croissante01(data)) # 1