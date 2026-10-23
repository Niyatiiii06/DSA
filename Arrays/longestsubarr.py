arr=[1,2,3,1,1,1,4]
k=3

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
    prefix_sum+=1

    if prefix_sum==k:
        max_len=i+1
    
    needed= prefix_sum- k
    if prefix_sum in prefixsum_map:
        length= i-prefixsum_map[needed]
        max_len= max(length,max_len)
    
    if prefix_sum not in prefixsum_map:
        prefixsum_map[prefix_sum]=i
print(max_len)

#OPTIMAL    
left=0
total=0
for i in range(len(arr)):
    total+=arr[i]

    if total==k:
        max_len=max(max_len,i-left+1)

    while total>k:
        total-=arr[left]
        left+=1
print(max_len)