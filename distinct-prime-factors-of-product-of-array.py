class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
        for num in nums:
            ans |= self.distFact(num)
        return len(ans)
            
            
            
            
    def distFact(self, num):
        
        d = 2
        ans = set()
        while d*d <= num:
            divides_num= False
            while num%d == 0:
                num/=d
                divides_num =  True
            if divides_num:
                ans.add(int(d))
            d+=1
        if num > 1:
            ans.add(int(num))
        return ans
