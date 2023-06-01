class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        pre = [1]*len(ratings)
        n = len(pre)
        i = n-1
        while i > 0:
            if ratings[i-1]>ratings[i]:
                pre[i-1] = pre[i]+1
            i-=1

        i = 0
        while i < n-1:
            if ratings[i+1]>ratings[i]:
                pre[i+1] = max(pre[i+1], pre[i]+1)
            i+=1
        print(pre)
        return sum(pre)