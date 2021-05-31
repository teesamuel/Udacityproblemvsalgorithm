def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) < 1 :
        return (-1,-1)

    lowest=ints[0]
    highest=ints[0]

    for item in ints:
        if ints[item] < lowest :
            lowest = ints[item]
        if ints[item] > highest:
            highest = ints[item]
    return (lowest,highest)

## Example Test Case
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


l = [i for i in range(0, 99)]  # a list containing 0 - 98
random.shuffle(l)

print ("Pass" if ((0, 98) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 80)]  # a list containing 0 - 79
random.shuffle(l)

print ("Pass" if ((0, 79) == get_min_max(l)) else "Fail")