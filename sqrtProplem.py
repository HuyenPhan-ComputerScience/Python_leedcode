def mySqrt(x):
    left = 1
    right = x
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if (mid ** 2) == x:
            return mid
        elif (mid ** 2) < x:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
            
    return result

print(mySqrt(35))
