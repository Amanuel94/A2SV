class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        comp = []

        for row in grid:
            i = 0
            to_app = []
            while i < len(row)-2:
                to_app.append(max(row[i:i+3]))
                i+=1
            comp.append(to_app)
        
        ans = [[0]*(len(grid)-2) for i in range((len(grid)-2))]

        i = 0
        while i < len(comp[0]):
            j = 0
            to_app = []
            while j < len(comp)-2:
                ans[j][i] = max(comp[j][i], comp[j+1][i], comp[j+2][i])
                j+=1
            
            i+=1
        return ans
