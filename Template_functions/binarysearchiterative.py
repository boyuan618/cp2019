def binarySearch(arr, left, right, target):
    while left < right:
        size = len(arr)
        mid = int((size/2)) +1
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1

arr = [1, 2, 4, 65, 4234]
print(binarySearch(arr, 0, len(arr)-1, 65))