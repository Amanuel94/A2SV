class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count = i = 0
        
        while tickets[k]:
            
            if tickets[i]:
                tickets[i]-=1
                count+=1
            if i < len(tickets)-1:
                i+=1
            else:
                i = 0
        return count
        