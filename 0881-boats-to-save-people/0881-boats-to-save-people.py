class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j = len(people)-1
        
        ans = 0
        
        while i < j:
            sum_ = people[i]+people[j]
            if sum_<= limit:
                i+=1
                j-=1
            else:
                j-=1
            ans+=1
            
        return ans + int(j ==  i)
    
        
        