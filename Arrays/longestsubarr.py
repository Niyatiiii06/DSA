arr=[1,2,3,1,1,1,4]
k=3

#with sum=k
#BRUTE
max_len=0
for i in range(len(arr)):
    total=0
    for j in range(i,len(arr)):
        total+= arr[j]
        if total==k:
            max_len=max(max_len,j-i+1)
print(max_len)

#BETTER-SLIDING WINDOW N HASHMAP
prefix_sum=0
prefixsum_map={}
for i in range(len(arr)):
    prefix_sum+=arr[i]

    if prefix_sum==k:
        max_len=i+1
    
    needed= prefix_sum- k
    if needed in prefixsum_map:
        length= i-prefixsum_map[needed]
        max_len= max(length,max_len)
    
    if prefix_sum not in prefixsum_map:
        prefixsum_map[prefix_sum]=i
print(max_len)

# #OPTIMAL    
left=0
total=0
for i in range(len(arr)):
    total+=arr[i]
    while total>k:
        total-=arr[left]
        left+=1
    if total==k:
        max_len=max(max_len,i-left+1)

print(max_len)

#with sum<=k 
arr=[2,5,1,7,10]
k=14

for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        if sum<=k:
            max_len= max(max_len,j-i+1)

j=0
max_len=0
for i in range(n):
    sum+=arr[i]
    while sum>k:
        sum-= arr[j]
        j+=1
    if sum<=k:
        max_len=max(max_len,i-j+1)


j=0
max_len=0
for i in range(n):
    sum+=arr[i]
    if sum>k:   #just decrease by 1 rather than until sum>=k it'll reduce tc
        sum-= arr[j]
        j+=1
    if sum<=k:
        max_len=max(max_len,i-j+1)

