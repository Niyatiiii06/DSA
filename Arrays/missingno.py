arr=[1,2,4,5]
#BRUTE
n=len(arr)+1 #cuz 1 is missing
for i in range(n+1):
    if i not in arr:
        print(i)
#OPTIMAL-1
expected_sum=n*(n+1)//2
sum=0
for j in arr:
    sum+=j
print(expected_sum-sum)
#OPTIMAL-2
xor1=0
xor2=0
for i in range(n+1): #n+1 is 6 so we can get 1 to 5
    xor1^=i
for j in arr:
    xor2^=j
print(xor1^xor2)

