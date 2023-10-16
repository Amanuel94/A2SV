class Solution:
    def countVowels(self, word: str) -> int:

        vowels = [-1] + [i for i, c in enumerate(word) if c in "aeiou"] + [len(word)]
        diff = []
        for v in range(1, len(vowels)):
            diff.append(vowels[v] - vowels[v-1])
            
        pre = [0]*(len(diff))
        pre[0] = diff[0]
        prev = diff[0]
        for i in range(1, len(pre)):
            pre[i] = diff[i] + pre[i-1]
        for i in range(1, len(pre)):
            pre[i] = pre[i] + pre[i-1]

        ans = 0
        for i in range(1, len(diff)):
            ans+=pre[i-1]*diff[i]
        return ans

        # 1*2 + 1*4 + 1*1 + 1*4 + 1*1
        #     + 2*4 + 2*1 + 2*4 + 2*1
        #           + 4*1 + 4*4 + 4*1
        #                 + 1*4 + 1*1
        #                       + 4*1