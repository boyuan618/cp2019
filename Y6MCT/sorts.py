#sorted arr [1, 2, 3, 4, 5, 6, 10]


#bubble sort
def bubble_Sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
    return arr


print(bubble_Sort([1,3,4,10,2,5,6]))


#merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left) #sort left
        merge_sort(right) #sort right
        
        i = j = k = 0
        
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i+=1
            else: 
                arr[k] = right[j] 
                j+=1
            k+=1        
        while i < len(left):
            arr[k] = left[i]
            k+=1
            i+=1
        while j < len(right):
            arr[k] = right[j]
            k+=1
            j+=1
    return arr
ar = merge_sort([1,3,4,10,2,5,6])
print(ar)


def insertion_Sort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
        
    return arr
        
arrs = [1,3,4,10,2,5,6]
print(insertion_Sort(arrs))


# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
        
    return arr

arss = [1,3,4,10,2,5,6]
print(quickSort(arss, 0, len(arss)-1))