class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        else:
            i = 0
            res = 0
            while i < len(grid)-2:
                j = 0
                while j < len(grid[0])-2:
                    sub = [row[j:j+3] for row in grid[i:i+3]]
                    # print(sub, i, j)
                    
                    if len(sub) < 3 or len(sub[0]) < 3:
                        j+=1
                        continue
                    
                    if len(set([sub[k//3][k%3] for k in range(9)])) < 9:
                        j+=1
                        continue
                        
                    if set([sub[k//3][k%3] for k in range(9)]) != set(range(1,10)):
                        j+=1
                        continue
                    
                    if sum(sub[0]) != 15 or sum(sub[1])!= 15:
                        j+=1
                        continue
                    
                    if sum([sub[0][0],sub[1][0], sub[2][0]])!= 15 or sum([sub[0][1],sub[1][1], sub[2][1]]) != 15:
                        j+=1
                        continue 
                    if sum([sub[0][0] ,sub[1][1], sub[2][2]]) != 15 or sum([sub[2][0],sub[1][1], sub[0][2]])!= 15:
                        j+=1
                        continue
                    
                    res+=1
                    j+=1

                i+=1
            return res
        
        
        
        