class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:

        sum_heap = [0]
        n = len(nums)
        state  = [0]*n

        segment = {i:i for i in range(n)}
        sum_of_segments = {i:0 for i in range(n)} 

        def getSegment(i):
            if i == segment[i]:
                return i

            segment[i] = getSegment(segment[i])
            return segment[i]
        answer = [0]*(n)
        i = n-1
        while i >= 1:
            
            toRemove = removeQueries[i]
            state[toRemove] = nums[toRemove]
            sum_of_segments[getSegment(toRemove)]+=nums[toRemove]

            if toRemove > 0 and state[toRemove-1] > 0:
                sum_of_segments[getSegment(toRemove-1)]+= sum_of_segments[getSegment(toRemove)]
                segment[getSegment(toRemove)] = getSegment(toRemove-1)

            if toRemove < n-1 and state[toRemove+1] > 0:
                sum_of_segments[getSegment(toRemove+1)]+= sum_of_segments[getSegment(toRemove)]
                segment[getSegment(toRemove)] = getSegment(toRemove+1)

            heappush(sum_heap, -sum_of_segments[getSegment(toRemove)])
            answer[i-1] = -sum_heap[0]
            i-=1

        return answer