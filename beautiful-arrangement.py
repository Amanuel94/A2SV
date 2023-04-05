class Solution:
    def countArrangement(self, n: int) -> int:
        
        
        ans = 0
        def countPerm(flag, cur_len, n):
            nonlocal ans
            # print(flag, ans)
            if cur_len == n:
                ans+=1
                return
            
            for i in range(n):
                
                if flag&1<<i == 0 and ((cur_len+1)% (i+1)  == 0 or (i+1) % (cur_len+1) == 0):
                    countPerm(flag|1<<i, cur_len+1, n)
                    
        countPerm(0, 0, n)
                    
        return ans
                    
            
