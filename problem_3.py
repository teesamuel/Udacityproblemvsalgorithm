def quicksort(sequence):
    """
    Sorts an Array  list .

    Args:
       sequence(list): Input List
    Returns:
       (sequence(list): Sorted List
    """
    if len(sequence) <2:
        return sequence
    else:
        pivot=sequence.pop(0)

    item_lower=[]
    item_higher=[]

    for item in sequence:
        if item < pivot:
            item_lower.append(item)
        else :
            item_higher.append(item)
    
    return quicksort(item_lower)+[pivot]+ quicksort(item_higher)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sortedlist=quicksort(input_list)
    if(len(sortedlist)) ==1:
        return [sortedlist[0],0]
    elif (len(sortedlist)) <1:
        return []

    flag=0
    first_output=""
    second_output=""
    for i in range(len(sortedlist) - 1, -1, -1):
        if flag==0:
            first_output += str(sortedlist[i])
            flag=1
        elif flag==1:
            second_output += str(sortedlist[i])
            flag=0
    return [int(first_output),int(second_output)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1], [0, 1]])
test_function([[0], [0, 0]])
test_case2 = [[0,0,0,0,0], [0, 0]]
test_case3 = [[], []]
test_function(test_case2)
test_function(test_case3)





