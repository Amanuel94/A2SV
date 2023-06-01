class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        """
        try to make runnning subsequences as long as possible by adding the current element to
        the shortest valid subsequence
        """

        sequence_length = [[] for _ in range(2001)]
        for num in nums:
            # print(sequence_length[:10], num)
            if sequence_length[(num-1)] :
                heappush(sequence_length[num], heappop(sequence_length[num-1])+1)
            else:
                heappush(sequence_length[num], 1)
     
        
        for len_ in sequence_length:
            if len_ and 0 < len_[0] < 3:
                return False
        return True