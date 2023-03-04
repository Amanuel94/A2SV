class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n = 10**9 + 7
        pre = [0]*(len(nums)+1)
        
        for request in requests:
            start, end = request
            pre[start]+=1
            pre[end+1]-=1
        i = 1
        while i < len(pre):
            pre[i]+=pre[i-1]
            i+=1
            

        pre.sort(reverse= True)
        nums.sort(reverse = True)
                
        ans = 0
        for i, num in enumerate(nums):
            ans+= (num*pre[i])%n
            
        return ans%n
        
        
            
        
            
            
        
        