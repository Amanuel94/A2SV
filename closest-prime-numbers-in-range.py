class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        primes  = self.primeSieve(right)
        ans = [-1, -1]
        prev = left
        min_diff = float('inf')
        
        while not primes[prev]:
            prev+=1
            if prev > right:
                return ans
        
        cur  = prev+1
        # print(primes)
        while cur <= right:
            if primes[cur] and primes[prev] and primes[cur] - primes[prev] < min_diff:
                
                ans = [prev, cur]
                min_diff = cur - prev
                
                prev = cur
                
                if min_diff <= 2:
                    return ans
            cur+=1
        return ans
        
            
        
        
        
    def primeSieve(self, n):
        
        # sieve from 1 to n
        
        isPrime = [1]*(n+1)
        isPrime[0] = isPrime[1] = 0
        
        i = 2
        
        
        while i*i <= n:
            
            if isPrime[i]:
                
                j = i*i
                
                while j <= n:
                    
                    isPrime[j] = 0
                    j+=i
                    
            i+=1
        return isPrime
    
        
        
