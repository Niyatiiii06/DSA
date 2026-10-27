arr=[2,3,2,2,4]
n=len(arr)
for i in range(n):
    count=0
    for j in range(n):
        if arr[i]==arr[j]:
            count+=1
            if count>n//2:
                print(arr[i])

#Better- hashmap
map={}
for i in arr:
    map[i]= map.get(i,0)+1
for i,count in map.items():
    if count>len(arr)//2:
        print(i)

#BOYER MOORE VOTING ALGO
element=None
count=0
for i in arr:
    if count==0:
        element=i
        count=1
    elif i==element:
        count+=1
    else:
        count-=1
count1=0
for i in arr:
    if i==element:
        count1+=1
if count1>len(arr)//2:
    print(element)
else:
    print(-1)
