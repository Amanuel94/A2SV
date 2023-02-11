n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i = j = 0

while i < n and j < m:
    if arr1[i] < arr2[j]:
        print(arr1[i], end = " ")
        i+=1
    else:
        print(arr2[j], end = " ")
        j+=1
while i < n:
    print(arr1[i], end = " ")
    i+=1
while j < m:
    print(arr2[j], end = " ")
    j+=1
