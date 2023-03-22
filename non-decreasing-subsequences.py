class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        ans_set = set()
        def subseq(nums, cur, cur_sub):
            
            nonlocal ans
            # print(cur_sub, cur)
            if cur >= len(nums):
                if len(cur_sub) > 1 and tuple(cur_sub) not in ans_set:
                    ans.append(cur_sub[:])
                    ans_set.add(tuple(cur_sub[:]))
                    
                return
             
            if not cur_sub or nums[cur] >= cur_sub[-1]: 
                cur_sub.append(nums[cur])
                subseq(nums, cur+1, cur_sub)
                if cur_sub:
                    cur_sub.pop()

            subseq(nums, cur+1, cur_sub)

        subseq(nums, 0, [])
            
        return ans
