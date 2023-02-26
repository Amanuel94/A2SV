class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        left = ans = 0
        fr = defaultdict(int)
        
        for right, right_f in enumerate(fruits):
            fr[right_f]+=1
            
            while len(fr) > 2:
                fr[fruits[left]]-=1
                if fr[fruits[left]] == 0:
                    del fr[fruits[left]]
                left+=1
            ans = max(ans, right-left+1)
        
        return ans
        
        