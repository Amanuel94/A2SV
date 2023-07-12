class Solution:
    def longestArithSeqLength(self, arr: List[int]) -> int:
        
        min_, max_ = sorted(arr)[0::len(arr)-1]
        max_len = float('-inf')
        
        for diff in range(-max_, max_+1):
            index = {}
            dp = [1]*len(arr)
            for i, num in enumerate(arr):        
                if num - diff in index:
                    dp[i] = dp[index[num-diff]]+1
                index[num] = i
            max_len = max(max_len, *dp)
        return max_len