# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = list(map(int, input().split()))
s = {}
for i in a:
    if i in s.keys():
        s[i]+=1
    else:
        s[i] = 1
for i in s.keys():
    if s[i] == 1:
        print(i)
        break
