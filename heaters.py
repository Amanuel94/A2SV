class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses = sorted(list(set(houses + heaters)))
        heaters.sort()
        
        def good(houses, heaters, k):
            i = j = 0
            while i < len(houses) and j < len(heaters):
                if j > 0:
                    if heaters[j-1]+k < houses[i] < heaters[j]-k:
                        return False

                    if houses[i] > heaters[j]+k:
                        j+=1
                    else:
                        i+=1
                else:
                    if houses[i] < heaters[0] - k:
                        return False
                    if houses[i] > heaters[0] + k:
                        j+=1
                    else:
                        i+=1
            return i == len(houses)



        low = 0
        high = max(houses[-1], heaters[-1])

        # print(bfs([1, 5, 10], [10], 5))
        while low <= high:
            mid = (low + high)//2
            if good(houses, heaters, mid):
                high = mid - 1
            else:
                low = mid + 1
        return low