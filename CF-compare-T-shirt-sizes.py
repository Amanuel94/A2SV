from collections import Counter
N = int(input())

for i in range(N):
    
    sizes  = input().split()
    
    size1 = sizes[0]
    size2 = sizes[1]
    
    num1 = Counter(size1)['X']+1
    num2 = Counter(size2)['X']+1
    
    if 'S' in size1:
        num1*=-1
    if 'S' in size2:
        num2*=-1
        
    if size1 == 'M':
        num1 = 0
        
    if size2 == 'M':
        num2 = 0
    
    if num1 > num2:
        
        print('>')
    elif num1 == num2:
        print('=')
    else:
        print('<')
        
    
    
    
    
