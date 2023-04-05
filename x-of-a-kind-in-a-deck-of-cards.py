class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        
        d = Counter(deck).items()
        cur_gcd = 0
        for i in d:
            
            if gcd(cur_gcd, i[1]) == 1:
                return False
            
            cur_gcd = gcd(cur_gcd, i[1])
            
        return True
        
