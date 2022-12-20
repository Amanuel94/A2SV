# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = {}

for i in range(n):
    t = input()
    if t not in arr.keys():
        arr[t] = 1
    else:
        arr[t]+=1
        
print(len(arr.items()))
print(" ".join(list(map(str, arr.values()))))
