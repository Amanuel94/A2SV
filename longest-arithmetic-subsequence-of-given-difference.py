class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:

        """
        for each element we track the number of arithmetic numbers it belongs to
        """

        tracker = [1]*len(arr)
        index = {}
        for i, num in enumerate(arr):
            if num - diff in index:
                tracker[i] = tracker[index[num-diff]]+1
            index[num] = i
        return max(tracker)