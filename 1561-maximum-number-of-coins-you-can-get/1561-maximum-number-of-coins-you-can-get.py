class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        sum_of_picks = 0
        for i in range(2*len(piles)/3):
            if i % 2:
                sum_of_picks+=piles[len(piles)-1-i]
        return sum_of_picks
        
        
        