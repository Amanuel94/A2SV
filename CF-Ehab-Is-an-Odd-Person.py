n = int(input())

arr = list(map(int, input().split()))

contains_even = contains_odd = False
for i in arr:
    if i % 2 == 0:
        contains_even = True
    if i % 2:
        contains_odd = True
    if contains_even and contains_odd:
        break
    
# print(contains_even, contains_odd)
if contains_even and contains_odd:
    arr.sort()
    print(" ".join(list(map(str, arr))))
else:
    print(" ".join(list(map(str, arr))))
