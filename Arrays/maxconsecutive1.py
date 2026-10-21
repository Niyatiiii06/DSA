arr=[1,1,0,0,1,0,1,1,1]
count=0
maximum=0
for i in arr:
    if i==1:
        count+=1
        maximum=max(maximum,count)
    else:
        count=0
print(maximum)