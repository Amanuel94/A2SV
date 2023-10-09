class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        

        def pollfirst(hash, p, first, k, m):
            idx = ord(first) - ord('a') + 1
            return (hash - idx*pow(p, k-1, m))%m
        
        def addLast(hash, p, last, m):
            idx = ord(last) - ord('a') + 1
            return (hash*p + idx)%m

        str_hash = 0
        s = "".join(reversed(s))

        for c in s[:k]:
            str_hash = addLast(str_hash, power, c, modulo)

       

        
        i, j = 0, k
        ans_i, ans_j = i, j
        while j < len(s):
            str_hash = pollfirst(str_hash, power, s[i], k,  modulo)
            i+=1
            str_hash = addLast(str_hash, power, s[j], modulo)
            j+=1
            if str_hash == hashValue:
                ans_i, ans_j = i, j

        return "".join(reversed(s[ans_i:ans_j]))