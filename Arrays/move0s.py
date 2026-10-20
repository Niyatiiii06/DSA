#move 0s to the end
arr=[1,2,8,0,0,9,0]
n= len(arr)
i=0
for j in range(n):
    if arr[j]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
print(arr)

#move 0s to front
arr=[1,2,0,8,9,0,0]
n=len(arr)
i=n-1
for j in range(n-1,-1,-1):
    if arr[j]!=0:
        arr[i]=arr[j]
        i-=1
while i>=0:
    arr[i]=0
    i-=1
print(arr)


#Linear Search
for i in range(n):
    if arr[i]==0:
        print(f'first 0 at {i} index')
        break
print('no 0s')
