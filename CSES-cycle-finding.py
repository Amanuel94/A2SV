import sys
def main():
    n, m = map(int, sys.stdin.readline().split())
 
    edges = []
    inf = float('inf')
    for _ in range(m):
        edges.append(list(map(int, sys.stdin.readline().split())))
    dist = [0 for _ in range(n+1)]
    par = [-1 for _ in range(n+1)]
    _ = 0
    x = 0
    while _ < n:
        if x == -1:
            break
        x = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                par[v] = u
                x = v
        _+=1
    if x == -1:
        print("NO")
    else:
        _ = 0
        while _ < n:
            x = par[x]
            _+=1
        cycle = [x]
        curNode = x
       
        while curNode != x or len(cycle) <= 1:
            curNode = par[curNode]
            cycle.append(curNode)
        
 
        print("YES")
        print(*(cycle[::-1]))
main()
