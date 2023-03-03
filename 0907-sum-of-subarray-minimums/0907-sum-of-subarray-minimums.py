class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
    
        
        # stack of tuples
        
        # simple case: num > stack[-1], append((num, 0))
        
        # if else, if x to pop:
            # ans += (1+x[1])*x[0]+(poppped)
            #keep track of num of being popped: +=x[1]+1
            
        arr.append(0)
        stack = []
        ans = 0
        n = 10**9+7
        for num in arr:
            if not stack or stack[-1][0] < num:
                stack.append((num, 0))
            else:
                popped = 0
                while stack and stack[-1][0] >= num:
                    x = stack.pop()
                    ans+=((1+x[1])*x[0]*(popped+1)) % n
                    popped+=(x[1]+1)
                stack.append((num, popped))
            # print(stack)
                    
        return ans%n
                    
            
         
            
        