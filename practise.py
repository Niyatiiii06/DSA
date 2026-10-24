# 1	Array traversal and indexing	—	Basic
# 2	Largest element in an array	—	Easy
# 3	Second largest distinct element	—	Easy
# 4	Smallest and second smallest distinct elements	—	Easy
# 5	Check if array is sorted	—	Easy
# 6	Remove duplicates from sorted array	26	Easy
# 7	Rotate array to the left by K	—	Basic
# 8	Rotate array to the right by K	189	Medium
# 9	Move zeroes to the end	283	Easy
# 10	Move zeroes to the front	—	Basic
# 11	Union of two sorted arrays	—	Basic
# 12	Intersection of two sorted arrays	—	Basic
# 13	Missing number — sum formula and XOR	268	Easy
# 14	Maximum consecutive ones	485	Easy
# 15	Single number using XOR	136	Easy
# 16	Longest subarray with sum K — brute force	No exact single match	Basic
# 17	Longest subarray with sum K — prefix sum + hashmap	No exact single match	Basic
# 18	Longest subarray with sum K — sliding window for non-negative elements	No exact single match	Basic
# 19	Maximum sum of K consecutive elements — fixed window	643 is related	Easy
# 20	Minimum window length with sum at least K	209	Medium
# 21	Longest subarray with sum at most K	No exact single match	Basic
# 22	Longest subarray with sum exactly K — sliding window for non-negative elements

arr=[0,1,1,0,3,2]
n=len(arr)
k=2
total=0
max_len=0
left=0
for i in range(n):
    total+=arr[i]

    while total>k:
        total-=arr[left]
        left+=1
    if total==k:
        max_len=max(max_len,i-left+1)
print(max_len)
#prefix_sum=0
# map={}
# for i in range(n):
#     prefix_sum+=arr[i]
#     if prefix_sum==k:
#         max_len=i+1
#     needed= prefix_sum-k
#     if needed in map:
#         length= i-map[needed]
#         max_len=max(max_len,length)
#     if prefix_sum not in map:
#         map[prefix_sum]=i
# print(max_len)
# for i in range(n):
#     total=0
#     for j in range(j,n):
#         if total==k:
#             max_len=max(max_len, j-i+1)


# xor=0
# for i in arr:
#     xor^=i
# print(xor)
# count=0
# for i in range(len(nums)):
#     num=nums[i]
#     for j in range(len(nums)):
#         if nums[j]==num:
#             count+=1
#             if count==1:
#                 print(count) 


# count=0
# maximum=0
# for i in arr:
#     if i==1:
#         count+=1
#         maximum=max(count,maximum)
# print(maximum)


# n=len(arr)
# xor=0
# xor1=0
# for i in arr:
#     xor^=i
# for i in range(n+1):
#     xor^=i
# print(xor^xor1)
# sum=n*(n+1)//2
# sum2=0
# for i in arr:
#     sum2+=i
# print(sum-sum2)



# arr1=[1,2,3,4,5]
# result=[]
# i=j=0
# while i<len(arr) and j<len(arr1):
#     if arr[i]==arr[j]:
#         num=arr[i]
#         i+=1
#         j+=1
#         if len(result)==0 or result[-1]!=num:
#             result.append(num)
# print(result)
#     if arr[i]<arr1[j]:
#         num=arr[i]
#         i+=1
#     else:
#         num=arr1[j]
#         j+=1
#     if len(result)==0 or result[-1]!=num:
#         result.append(num)
# while i<len(arr):
#     num=arr[i]
#     if len(result)==0 or result[-1]!=num:
#         result.append(num)
#         i+=1
# while j<len(arr1):
#     num=arr1[j]
#     if len(result)==0 or result[-1]!=num:
#         result.append(num)
#         j+=1
# print(result)


# n=len(arr)
# j=n-1
# for i in range(n-1,-1,-1):
#     if arr[i]!=0:
#         arr[j]=arr[i]
#         j-=1
# while j>=0:
#     arr[j]=0
#     j-=1
# print(arr)
#     if arr[i]!=0:
#         arr[i],arr[j]=arr[j],arr[i]
#         j+=1
# print(arr)


# k=2
# n=len(arr)#6
# temp=arr[n-k:]
# k=k%n
# for i in range(n-1,k-1,-1):
#     arr[i]=arr[i-k]
# for i in range(k):
#     arr[i]=temp[i]
# print(arr)
# for i in range(n-k):
#     arr[i]=arr[i+k]
# for i in range(n-k,n):
#     arr[i]=temp[i-(n-k)]
# print(arr)


# def is_sorted(arr):
#     for i in range(1,len(arr)):
#         if arr[i]<arr[i-1]:
#             return False
#     return True
# print(is_sorted([1,3,4,6,7]))
    

# largest=float('inf')
# s_lar=float('inf')
# for i in range(len(arr)):
#     if largest>arr[i]:
#         s_lar= largest
#         largest=arr[i]
#     elif arr[i]<s_lar:
#         s_lar=arr[i]
# print(s_lar)
# print(largest)