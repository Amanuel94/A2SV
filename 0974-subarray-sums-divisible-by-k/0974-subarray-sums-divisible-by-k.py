class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        pre = [0]
    
        for num in nums:
            pre.append((pre[-1]+num)%k)
            
        d = defaultdict(int)
        ans = 0
        
        for i in pre:
            ans+=d[i]
            d[i]+=1
            
        return ans
            
        
        