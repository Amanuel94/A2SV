class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        
        attackers = []
        i = king[0]
        while i < 8:
            if [i, king[1]] in queens:
                attackers.append([i, king[1]])
                break
            i+=1
        i = king[0]
        while i > -1:
            if [i, king[1]] in queens:
                attackers.append([i, king[1]])
                break
            i-=1
        i = king[1]
        while i < 8:
            if [king[0], i] in queens:
                attackers.append([king[0], i])
                break
            i+=1
        i = king[1]
        while i > -1:
            if [king[0], i] in queens:
                attackers.append([king[0], i])
                break
            i-=1
            
        i = king[0]
        d_sum = king[0]+king[1]
        while i < 8 and d_sum - i > -1:
            if [i, d_sum-i] in queens:
                attackers.append([i, d_sum-i])
                break
            i+=1
        i = king[0]
        while i > -1 and d_sum - i < 8:
            if [i, d_sum-i] in queens:
                attackers.append([i, d_sum-i])
                break
            i-=1
            
        i = king[0]
        d_diff = king[0] - king[1]
        while i < 8 and i - d_diff < 8:
            if [i, i- d_diff] in queens:
                attackers.append([i, i- d_diff])
                break
            i+=1
            
        i = king[0]
        while i > -1 and i -d_diff > -1:
            if [i, i-d_diff] in queens:
                attackers.append([i, i-d_diff])
                break
            i-=1
            
        
        return attackers
    