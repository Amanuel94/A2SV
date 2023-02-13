class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        
        i = len(players)-1
        j = len(trainers)-1
        
        ans=  0
        
        while i >= 0 and j >= 0:
            if players[i] <= trainers[j]:
                i-=1
                j-=1
                ans+=1
            else:
                i-=1
        return ans
                
                