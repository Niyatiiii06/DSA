arr=[1,1,2,3,2]
n=len(arr)

#BRUTE
for i in range(n):
    count=0
    num=arr[i]
    for j in range(n):
        if arr[j]==num:
            count+=1
    if count==1:
        print(num)

#OPTIMAL
result=0
for i in arr:
    result^=i
print(result)