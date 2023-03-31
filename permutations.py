class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def binToPerm(flag, curr, nums):
            nonlocal ans
            
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                
                if flag&(1<<i)==0:
                    curr.append(nums[i])
                    flag|=(1<<i)
                    binToPerm(flag, curr, nums)
                    flag&=~(1<<i)
                    curr.pop()
                    # binToPerm(flag, curr, nums)
                              
        binToPerm(0, [], nums)
                    
        return ans
