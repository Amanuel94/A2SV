n, k  = list(map(int, input().split()))
 
seq = list(map(int, input().split()))
seq.sort()
 
if 0 < k < n and seq[k-1] < seq[k]:
    print(seq[k-1])
elif 0 < k < n and seq[k-1] == seq[k]:
    print(-1)
elif k == 0:
    print(seq[0]-1 or -1)
else:
    print(seq[-1])
