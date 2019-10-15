def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[j],arr[j+1:i+1] = arr[i],arr[j:i]
                break
    
    return arr

arr = [1, 34, 54565, 234, 1321, 13, 34]
print(insertionSort(arr))