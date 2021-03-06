def binarySearch(arr, left, right, target):
    
    print("Running in process")
    if right >= 1:
        size = len(arr)
        mid = int(size/2) + 1
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            return binarySearch(arr, left, mid-1, target)
        
        else:
            return binarySearch(arr, mid+1, right, target)
    
    else:
        return -1
        
arr = [1, 234, 433, 4565, 7565]
print(binarySearch(arr, 0, len(arr)-1, 4565))