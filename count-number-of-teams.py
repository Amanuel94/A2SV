class Solution:
    def numTeams(self, nums: List[int]) -> int:

        n = len(nums)
        ltr = [0]*n
        rtl = [0]*n

        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    ltr[i]+=1
                if nums[n-j-1] > nums[n-i-1]:
                    rtl[n-i-1]+=1
        
        # print(ltr, rtl)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    count+=ltr[j]
                if nums[n-1-i] < nums[n-1-j]:
                    count+=rtl[n - 1 -j]
        return count