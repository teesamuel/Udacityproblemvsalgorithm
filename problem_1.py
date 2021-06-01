def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number ==0 or number ==1:
        return number
    if number < 1:
        return 0

    start = 1
    end = number
    while (start <= end):
        
        midPoint = (start + end ) // 2
        # check for perfect sQUare
        if (midPoint * midPoint == number):
            return midPoint
        #since we are looking for the floor, the first lowest value will be our answer 
        if midPoint * midPoint < number:
            start = midPoint + 1
            answer=midPoint
        else:
            end= midPoint -1
    return answer
    

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (0 == sqrt(-1)) else "Fail")
print ("Pass" if  (0 == sqrt(-99)) else "Fail")
print ("Pass" if  (999999== sqrt(999999999999)) else "Fail")
