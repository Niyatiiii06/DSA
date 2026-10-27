arr=[-2,-3,4,5,-1,4]
max_total=0
for i in range(len(arr)):
    total=0
    for j in range(i,len(arr)):
        total+=arr[j]
        max_total= max(max_total,total)
print(max_total)

#KADANE'S ALGORITHM
maxi=float('-inf')
sum=0
for i in range(len(arr)):
    sum+=arr[i]
    if sum>maxi:
        maxi=sum
    elif sum<0:
        sum=0
print(maxi)

start=0 #to print the subarray
ans_start=-1
end=-1
for i in range(len(arr)):
    sum+=arr[i]
    if sum==0:
        start=i
    elif sum>maxi:
        maxi=sum
        ans_start=start
        end=i
    elif sum<0:
        sum=0
        start=i+1
print(maxi,ans_start,end)