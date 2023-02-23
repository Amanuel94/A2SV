class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """                                




        pre = [0]
                           
        for i in nums:
            pre.append(pre[-1]+i)
            
            
        sums = {}
        ans = 0
        for i in pre:
            if  i - k in sums:
                ans+=sums[i-k]
                
            if i in sums:
                sums[i]+=1
            else:
                sums[i]=1
        return ans
                
                
        
            
        
        
        