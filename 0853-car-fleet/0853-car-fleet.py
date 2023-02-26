class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = zip(position, speed)
        cars.sort(key = lambda x: x[0], reverse = True)
        
        top = float('-inf')
        fleets = 0
        
        for car in cars:
            time = (target - car[0])/float(car[1])
            if time > top:
                top = time
                fleets+=1
        return fleets
                
            