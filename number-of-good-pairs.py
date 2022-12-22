class Solution(object):
    def numIdenticalPairs(self, nums):
        out = 0
        for i in Counter(nums).items():
            out+= i[1]*(i[1]-1)/2
        return out
