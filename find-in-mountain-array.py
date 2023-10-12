# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:


        low, high = 0, mountain_arr.length()-1
        peak = -1
        while low < high:
            mid = (low + high)//2
            left = mountain_arr.get(mid-1) if mid > 0 else -inf
            val = mountain_arr.get(mid)
            right = mountain_arr.get(mid+1) if mid < mountain_arr.length()-1 else inf
            if left < val < right:
                low = mid + 1
            elif left  > val > right:
                high = mid-1
            else:
                peak = mid
                break
            peak = low

        
        low, high = 0, peak
        count = 0
        while low <= high:
            mid = (low + high)//2
            val = mountain_arr.get(mid)

            if  val < target:
                low = mid + 1
            elif target < val:
                high = mid-1
            else:
                return mid

        low, high = peak+1, mountain_arr.length()-1
        while low <= high:
            mid = (low + high)//2
            val = mountain_arr.get(mid)

            if  val > target:
                low = mid + 1
            elif target > val:
                high = mid-1
            else:
                return mid

        return -1