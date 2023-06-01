class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        """
        use a varable trace with value <= current index
        """

        arr.sort()
        i = 1
        trace = 1
        while i < len(arr):
            if trace+1 <= arr[i]:
                trace+=1
            i+=1
        return trace