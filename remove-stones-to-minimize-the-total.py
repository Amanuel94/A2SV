class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        i = sum_ = 0
        while i < len(piles):
            sum_ += piles[i]
            piles[i]*=-1
            i+=1
        heapify(piles)
        while k:
            x = -heappop(piles)
            heappush(piles, -x+x//2)
            sum_ -=x//2
            k-=1
        return  sum_