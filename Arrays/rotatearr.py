#left rotate Arrays by 1place
arr=[1,2,3,4,5]
temp=arr[0]
for i in range(1,len(arr)):
    arr[i-1]=arr[i]
arr[-1]=temp
print(arr)

#right rotate Arrays by 1place
temp=arr[len(arr)-1]
arr=[1,2,3,4,5]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=temp
print(arr)

#left rotate by k values
k=2
arr=[1,2,3,4,5]
n=len(arr)#5
temp=arr[:k%n]
for i in range(n-k):
    arr[i]=arr[i+k]
for i in range(n-k,n):
    arr[i]=temp[i-(n-k)]
print(arr)

#rotate right by k values eg12
k=12
arr=[1,2,3,4,5]
n=len(arr)#5
k=k%n #2
temp=arr[n-k:]
for i in range(n-1,k-1,-1):
    arr[i]=arr[i-k]
for i in range(k):
    arr[i]=temp[i]
print(arr)


