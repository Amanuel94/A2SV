class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        r = len(numbers)-1
        l = 0
        
        while  l < r:
            sum_= numbers[l] + numbers[r]
            if sum_ == target:
                return [l+1,r+1]
            
            elif sum_ < target:
                l+=1
            else:
                r-=1
        return -1