class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        
        d = {tuple(interval): i for i, interval in enumerate(intervals)}
    
        
        ans = [-1]*len(intervals)
        
        flag =  False
        
        intervals.sort()
        
        for interval in intervals:
            
            low = 0
            high = len(intervals)-1
            
            while low <= high:
                mid = (low+high)//2
                
                if intervals[mid][0] == interval[1]:
                    ans[d[tuple(interval)]] = d[tuple(intervals[mid])]
                    flag = False
                    break
                    
                elif intervals[mid][0] < interval[1]:
                    
                    low =  mid + 1
                    
                else:
                    flag = True
                    store =  mid
                    high = mid-1
                
            if flag:
                ans[d[tuple(interval)]] = d[tuple(intervals[store])]
            flag =  False
        return ans
            
            
            
        
        
                
                