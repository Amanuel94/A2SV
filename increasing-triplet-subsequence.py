class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        """
        make the first and the second numbers as close as possible
        """
        
        numi, numj = float('inf'), float('inf')

        for num in nums:
            if num > numj:
                return True
            if num > numi:
                numj = min(num, numj)
            else:
                numi = num
        return False