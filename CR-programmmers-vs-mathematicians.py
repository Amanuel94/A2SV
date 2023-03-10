t =  int(input())

for _ in range(t):
    
    a, b = list(map(int, input().split()))
    
    
    low = 0
    
    high = min(a, b)
    
    store= 0 
    
    while low <= high:
        
        mid = low + (high - low)//2
        
        if a+b >= 4*mid:
            store  = mid
            low = mid+1
        else:
            high = mid-1
    
    print(store)
