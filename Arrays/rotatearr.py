# #left rotate Arrays by 1place
# arr=[1,2,3,4,5]
# temp=arr[0]
# for i in range(1,len(arr)):
#     arr[i-1]=arr[i]
# arr[-1]=temp
# print(arr)

# #right rotate Arrays by 1place
# temp=arr[len(arr)-1]
# arr=[1,2,3,4,5]
# for i in range(len(arr)-1,0,-1):
#     arr[i]=arr[i-1]
# arr[0]=temp
# print(arr)

# #left rotate by k values
# k=2
# arr=[1,2,3,4,5]
# n=len(arr)#5
# temp=arr[:k%n]
# for i in range(n-k):
#     arr[i]=arr[i+k]
# for i in range(n-k,n):
#     arr[i]=temp[i-(n-k)]
# print(arr)

#ABOVE HAS OPTIMAL TC(0(N)) BUT SC(O(K)) CUZ TEMP SO NOW 
# WE REMOVE TEMP AND USE REVERSE MTHOD HERE TC MORE 0(2N) BUT SC LESS 0(1)
def reverse(arr,left,right):
    while left<right:
        arr[left],arr[right]= arr[right],arr[left]
        right-=1
        left+=1
# def rotate_right(arr,k):
#     n=len(arr)
#     if n==0:
#         return arr
#     k=k%n
#     reverse(arr,0,n-1)
#     reverse(arr,0,k-1)
#     reverse(arr,k,n-1)
#     return arr
def rotate_left(arr,k):
    n=len(arr)
    if n==0:
        return arr
    k=k%n
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    return arr


arr = [1, 2, 3, 4, 5]
# print(rotate_right(arr, 12))
print(rotate_left(arr, 12))

# #rotate right by k values eg12
# k=12
# arr=[1,2,3,4,5]
# n=len(arr)#5
# k=k%n #2
# temp=arr[n-k:]
# for i in range(n-1,k-1,-1):
#     arr[i]=arr[i-k]
# for i in range(k):
#     arr[i]=temp[i]
# print(arr)


