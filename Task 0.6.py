from re import I


def max(*numbers):
    maximum = 0
    for i in numbers:
        if i >= maximum:
            maximum = i
    return maximum 

print(max(4, 7, 42, 22, 70, 85, 9))