class Solution:
    def minOperations(self, nums: List[int]) -> int:
        

        n = len(nums)
        nums = list(set(nums))    
        nums.sort()
        queue = deque([nums[0]])
        max_len = 1
        i = 1
        while i < len(nums):
            if not queue or nums[i] < queue[0] + n:
                queue.append(nums[i])
                i+=1
            else:
                queue.popleft()
            max_len = max(max_len, len(queue))
        return n - max_len