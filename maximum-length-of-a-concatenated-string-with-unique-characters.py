class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        max_ = float('-inf')
        
        def check_occ(strs, s):
            
            if len(s) > len(set(s)):
                return False
            
            str_ = set("".join(strs))
            for i in s:
                if i in str_:
                    return False
            return True

        
        def merger(arr, cur, strs = []):
            nonlocal max_
            
            if cur == len(arr):
                ans = 0
                for s in strs:
                    ans+=len(s)
                    
                max_ =  max(max_, ans)
                
                return
            
            if check_occ(strs, arr[cur]):
                strs.append(arr[cur])
                merger(arr, cur+1, strs)
                strs.pop()
            merger(arr, cur+1, strs)
        merger(arr, 0, [])
        return max_
                    
