n = int(input())

sources = list(range(1, n+1))
sinks =  []
for _ in range(n):
    isSource = False
    for i, deg in enumerate(list(map(int, input().split()))):
        
        if deg:
            if i+1 in sources:
                 sources.remove(i+1)
            isSource = True
           
    if not isSource:
        sinks.append(_+1)
sources.sort()
sinks.sort()
print(len(sources), end = ' ')
print(*sources)
print(len(sinks), end = ' ')
print(*sinks)
