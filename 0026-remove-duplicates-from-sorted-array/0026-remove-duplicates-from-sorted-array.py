class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] == nums[r]:
                if l!= r:
                    nums[r] = 101
                r+=1
            elif l < r:
                l+=1
        # nums.sort()
        
        # return nums.index(101)
        l = 0
        r = 1
        
        while r < len(nums):
            if nums[r] == 101:
                r+=1
            elif l < r and nums[l] != 101:
                l+=1
            elif l == r:
                r+=1
            if r< len(nums) and nums[l] == 101 and nums[r] < 101:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
        nums.append(101)
        return nums.index(101) if len(nums) -1 else 1
            
        
                
        
        