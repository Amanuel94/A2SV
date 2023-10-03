class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                char_, freq =  stack.pop()
                if freq < k - 1:
                    stack.append((char_, freq+1))
            else:
                stack.append((c, 1))
        return ("".join(map(lambda x: x[0]*x[1], stack)))