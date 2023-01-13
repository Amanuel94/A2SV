class Solution(object):
    def findTheWinner(self, n, k):
        arr = [i + 1 for i in range(n)]
        i = 1
        while len(arr) > 1:
            if i%k == 0:
                arr = arr[1:]
            else:
                arr = arr[1:] + [arr[0]]
            i+=1
        return arr[0]
