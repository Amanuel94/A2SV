# recieve A
A = set(list(map(int, input().split())))

# recieve the sets to be compared to A
n = int(input())
given = []
for i in range(n):

    set_ = set(list(map(int, input().split())))
    given.append(set_)

for i, set_ in enumerate(given):

    if len(set_) >= len(A):
        print(False)
        break
    
    elif not (A & set_) == set_:
        print(False)
        break
    
    if i ==  len(given)-1:
        print(True)
