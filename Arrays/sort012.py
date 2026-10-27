arr=[1,2,1,2,0,0,2]
count_0=count_1=count_2=0
for i in arr:
    if i==0: count_0+=1
    if i==1: count_1+=1
    if i==2: count_2+=1
pos=0
for j in range(count_0):
    arr[pos]=0
    pos+=1
for j in range(count_1):
    arr[pos]=1
    pos+=1
for j in range(count_2):
    arr[pos]=2
    pos+=1
print(arr)

#DUTCH NATIONAL FLAG- 3PTR
class Solution(object):
    def sortColors(self, nums):
        low=0
        mid=0
        high=len(nums)-1
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1 