class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        if rowIndex == 0:
            return [1]
        
        
        ans = []
        prev =  self.getRow(rowIndex-1)
        ans.append(1)
        for i in range(1, rowIndex):
            
            ans.append(prev[i-1]+ prev[i])
            
        ans.append(1)
        return ans
