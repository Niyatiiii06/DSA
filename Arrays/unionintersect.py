a=[1,2,3,4,5]
b=[1,2,2,4,6,6]

#BRUTE UNION
# union=set()
# for i in a:
#     union.add(i)
# for i in b:
#     union.add(i)
# print(sorted(union))

#OPTIMAL UNION
i=j=0
result=[]
while i<len(a) and j<len(b):
    if a[i]<= b[j]:
        num=a[i]
        i+=1
    else:
        num=b[j]
        j+=1

    if len(result)==0 or result[-1]!= num:
        result.append(num)

while i<len(a): #if b done but a left
    if len(result)==0 or result[-1]!=a[i]:
        result.append(a[i])
    i+=1
while j<len(b): #if a done but b left
    if len(result)==0 or result[-1]!=b[j]:
        result.append(b[j])
    j+=1

print(result)

#BRUTE INTERSECTION
def intersection_better(a, b):
    set_b = set(b)
    result = []

    for num in a:
        if num in set_b and (not result or result[-1] != num):
            result.append(num)

    return result

#OPTIMAL INTERSECTION
i=j=0
result=[]
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        i+=1
    elif b[j]<a[i]:
        j+=1
    else:
        if not result or result[-1]!=a[i]:
            result.append(a[i])

        i+=1
        j+=1
print(result)