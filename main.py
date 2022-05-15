'''
def findLargest(L):
    #return(max(L))
    low = 0
    high = len(L)-1

    if high == low:
        return L[low]
        
    #m = len(L)//2    
    mid = L[len(L)//2]
    #mid = low + (high-low) // 2
    print(low, mid, high)
    
    if (mid == 0 and L[mid] > L[mid+1]):
        return L[mid]

    if (mid < high and L[mid+1] < L[mid] and mid > 0 and L[mid] > L[mid-1]):
        return L[mid]
    
    if L[low] > L[mid]:
        return findLargest(L[:mid-1])
    else:
        return findLargest(L[mid+1:])
    

print(findLargest([7, 8, 2, 4, 5, 6]))
'''

def findLargest(L):
    left = 0
    right = len(L) - 1

    while (left < right):
        mid = left + (right-left) // 2

        if (L[left] < L[mid]):
            left = mid
        elif (L[left] > L[mid]):
            right = mid-1
        else:
            left += 1

    return L[left]

print(findLargest([7, 8, 2, 4, 5, 6]))