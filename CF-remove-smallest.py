T = int(input())

for i in range(T):
    n = int(input())
    
    a = list(map(int, input().split()))
    a.sort()
    
    i = 0
    while i < n-1:
        if  a[i+1] - a[i] < 2:
            i+=1
        else:
            print("NO")
            break
    if i == n-1:
        print("YES")
