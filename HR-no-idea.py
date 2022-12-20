# Enter your code here. Read input from STDIN. Print output to STDOUT
a,b = input().split()
arr = input().split()
A=set(input().split())
B=set(input().split())
count = 0
for i in arr :
    if i in A:
        count += 1
    elif i in B:
        count -= 1 
print(count)
