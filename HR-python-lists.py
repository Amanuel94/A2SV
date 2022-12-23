if __name__ == '__main__':
    N = int(input())
    
arr = []


for i in range(N):
    
    opr = input().split(" ")
    
    if 'insert' == opr[0]:
        
        index = int(opr[1])
        val = int(opr[2])
        
        arr.insert(index, val)
        
    elif opr[0] == "print" :
        
            
        print(arr)
        
    elif opr[0] == "remove":
        
        index = int(opr[1])
        arr.remove(index)
        
    elif opr[0] == "append":
        
        val = int(opr[1])
        arr.append(val)
        
    elif opr[0] == "pop":
        
        arr.pop()
        
    elif opr[0] == "reverse":
        
        arr.reverse()
        
    elif opr[0] == "sort":
        
        arr.sort()
