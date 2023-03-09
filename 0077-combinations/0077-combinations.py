class Solution(object):
    def combine(self, n, k, ans  = [[]]):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 0:
            return ans
        
        else:
            
            res = []

            for a  in ans:
                
                if a:
                    for i in range(a[-1]+1, n-k+2):
                        res.append(a + [i])
                    
                else:
                    for i in range(1, n-k+2):
                        
                        res.append([i])
                        
            return self.combine(n, k-1, res)

            
                        
                        
        
        