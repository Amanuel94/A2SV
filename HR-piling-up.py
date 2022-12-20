# Enter your code here. Read input from STDIN. Print output to STDOUT


def stack(st, size):
    tot = 0
    i, j = 0, len(st) -1
    while tot < len(st):
        if not tot:
            if st[i] > st[j]:
                top = i
                i+=1
                
            else:
                top = j
                j-=1
                
        else:
            if st[i] > st[j] and st[i] <= st[top]:
                top = i
                i+=1
                
            elif st[j] <= st[top]:
                top = j
                j-=1
                
            else:
                return "No"
        tot+=1
    return "Yes"
    
for T in range(int(input())):
    size =  int(input())
    arr = list(map(int, input().split()))
    print(stack(arr, size))
