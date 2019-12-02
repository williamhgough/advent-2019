# 1 = addition
# 2 = multiplication
# 99 = stop
# every 4 indexes == new operation
# Position 1 indicates first value index
# Position 2 indicates second value index
# Position 3 indicates where to put the output of previous calculation

ADDITION = 1
MULTIPLICATION = 2
STOP = 99


def calculate(intcode):
    intcode[1] = 12
    intcode[2] = 2
    opCode, index = intcode[0], 0

    while opCode != STOP:
        opCode = intcode[index]
        first = intcode[index+1]
        second = intcode[index+2]
        storeAt = intcode[index+3]

        if opCode == ADDITION:
            intcode[storeAt] = intcode[first] + intcode[second]
        elif opCode == MULTIPLICATION:
            intcode[storeAt] = intcode[first] * intcode[second]
        elif opCode == STOP:
            break
        else:
            print("something went really wrong")
            break
        index += 4

    return intcode[0]


with open("input.txt") as file:
    intcode = [int(x) for x in file.read().split(",")]
    print(calculate(intcode[:]))
