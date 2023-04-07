n  = int(input())
sum_deg =  0
for _ in range(n):
    
    for deg in list(map(int, input().split())):
        sum_deg+=deg

print(sum_deg//2)
