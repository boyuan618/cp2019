def mergeSort(arr):
    size = len(arr)
    if size > 2:
        mid = int(size//2)
        Left = arr[:mid]
        Right = arr[mid:]
        
        
        mergeSort(Left)
        mergeSort(Right)
        
        