class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def dp(s, i, j):
            if i == j:
                return 1
            if i == j-1:
                return 2 if s[i] == s[j] else 1
            
            if s[i] == s[j]:
                return  dp(s, i+1, j-1)+2
            else:
                return max(dp(s, i, j-1), dp(s, i+1, j))

        return dp(s, 0, len(s)-1)