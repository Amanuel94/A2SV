class Solution(object):
    def PredictTheWinner(self, nums, turn = True, off = 0):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # print(nums, turn, off)
        if len(nums) < 2:
            return True
        
        if turn:
            if len(nums) == 2:
                return max(nums)+off >= min(nums)
            else:
                return self.PredictTheWinner(nums[1:], False, off+nums[0]) or self.PredictTheWinner(nums[:-1], False, off+nums[-1])
               
                
                    
        else:
            if len(nums)==2:
                return min(nums)+off >= max(nums)
            else:
                return self.PredictTheWinner(nums[1:], True, off-nums[0]) and self.PredictTheWinner(nums[:-1], True, off-nums[-1])
               
            
        
