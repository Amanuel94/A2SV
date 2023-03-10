class Solution:
    
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        max_ = float('inf')
        trial = [0] * k 
        
        def backtrack(trial, counter, n, cookies):
            nonlocal max_
            if counter == n:
                max_ = min(max_, max(trial))
                return
            
            
            for i in range(k):
                trial[i] += cookies[counter]
                if max(trial) < max_:
                    backtrack(trial, counter + 1, n , cookies)
                    
                trial[i] -= cookies[counter]
                

        backtrack(trial, 0 , n, cookies)
        return max_