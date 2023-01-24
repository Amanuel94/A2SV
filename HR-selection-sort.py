n,m = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0

c = []

while i + j < n +  m:
    if i < n and j < m and a[i] < b[j]:
        c.append(a[i])
        i+=1
    elif  i < n and j < m and a[i] >= b[j]:
        c.append(b[j])
        j+=1
    elif i == n:
        c.append(b[j])
        j+=1
    elif j == m:
        c.append(a[i])
        i+=1
        
print(" ".join(list(map(str, c))))
    

    
    
    
    
