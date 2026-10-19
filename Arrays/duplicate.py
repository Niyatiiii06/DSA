def is_sort(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def remove_duplicates(arr):
    #return list(set(arr))
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1


print(is_sort([1, 2, 3, 4, 5]))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))