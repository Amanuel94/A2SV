class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        
        # sort both lists so that growTime is in descending
        combined = zip(plantTime, growTime)
        sorted_combined = sorted(combined, key=lambda x: x[1], reverse = True)
        plantTime, growTime = zip(*sorted_combined)
        
        
        # the amount of time for the whole operation until blooming is p + g
        plantStart = earliestDay = 0
        for i, p in enumerate(plantTime):
            plantStart = plantStart+p
            earliestDay = max(earliestDay, plantStart + growTime[i])
  
        return earliestDay
            


