t =  int(input())
 
for _ in range(t):
 
    num = bin(int(input()))[2:]
 
    ones = []
    first_zero = 0
    for i, b in enumerate(num):
 
        if b == '1':
            ones.append(i)
        else:
            first_zero = i
    y = ''
 
    if num == '1':
        print(3)
 
    elif len(ones) > 1:
 
        for i, b in enumerate(num):
 
            if i == ones[-1]:
                y = y + '1'
            else:
                y = y + '0'
        print(int(y, 2))
    else:
        
        for i, b in enumerate(num):
            if i == first_zero or i == ones[-1]:
                y = y + '1'
            else:
                y = y + '0'
        print(int(y, 2))
