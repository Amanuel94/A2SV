n,m  = list(map(int, input().split()))

arr1 =list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i = 0
j = 0

ans = [0]*m
while i < n and j < m:
    if arr1[i] < arr2[j]:
        ans[j]+=1
        i+=1
    else:
        j+=1
        if j < m:
            ans[j] = ans[j-1]
if j < m:   
    temp = ans[j]  
    while j < m:
        ans[j] =  temp
        j+=1

for i in ans:
    print(i, end = " ")
