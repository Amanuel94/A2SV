class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        range_sum = [0]*102
        for start , end in logs:
            range_sum[start - 1950]+=1
            range_sum[end - 1950]-=1
        pre = ans =  year = 0
        # print(range_sum)
        for i, num in enumerate(range_sum):
            pre+=num
            # print(pre, 1950+i)
            if pre > ans:
                
                year = 1950 + i 
                ans = pre
        return year
        
        