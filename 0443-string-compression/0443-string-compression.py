class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        prev = 0
        cur = 1
        rep = 1
        while cur < len(chars):
            if chars[prev] == chars[cur]:
                rep+=1
                chars.pop(cur)
            else:
                if rep > 1:
                    for c in list(str(rep)):
                        chars.insert(cur,c)
                        prev+=1
                        cur+=1
                rep = 1
                prev+=1
                cur+=1
        if rep -1:
                chars.extend(list(str(rep))) 
        return len(chars)