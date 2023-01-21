class Solution(object):
    def pancakeSort(self, arr):
        nums = sorted(arr)
        pancake = []
        for i in range(len(nums)):
            if arr[-1-i] == nums[i]:
                continue
            else:
                pancake.append(arr.index(nums[i]) + 1)
                arr = list(reversed(arr[:pancake[-1]])) + arr[pancake[-1]:]
                pancake.append(len(arr)-i)
                arr = list(reversed(arr[:pancake[-1]])) + arr[pancake[-1]:]
                print(arr)
        pancake.append(len(arr))
        return pancake