arr=[2,3,6,5,8,11]
target=14
n=len(arr)
def tsum(arr,target):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return i,j
print(tsum([2,3,6,5,8,11],14))

#BETTER
def t_sum(arr,target):
    n=len(arr)
    l=0
    r=n-1
    arr.sort()
    while l<r:
        total=arr[l]+arr[r]
        if total==target:
            return l,r
        if total>target:
            r-=1
        else:
            l+=1
print(t_sum([2,3,6,5,8,11],14))
#OPTIMAL
map={}
total=0
for i,n in enumerate(arr):
    needed= target-n
    if needed in map:
        print(map[needed],i)
    else:
        map[n]=i
