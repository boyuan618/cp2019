#linearsearch
def linearSearch(arr, target):
    
    for i in arr:
        if i == target:
            return arr.index(i)
        
arr = [4, 2, 5, 3, 7]
print(linearSearch(arr, 7))