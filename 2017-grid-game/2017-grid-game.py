class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        pre = [[0], [0]]
        
        for i in range(len(grid[0])):
            pre[0].append(pre[0][-1] + grid[0][i])
            pre[1].append(pre[1][-1] + grid[1][i])
            
            
        i = 1
        max_index = 0
        max_ = float('inf')
        
        while i < len(pre[0]):
            max_of_parts = max(pre[0][-1] -  pre[0][i], pre[1][i-1])
            if max_of_parts < max_:
                max_ =  max_of_parts
                max_index = i
            i+=1
                
        return max(pre[0][-1]- pre[0][max_index], pre[1][max_index-1])
            
            
            
            
            
        
        
        