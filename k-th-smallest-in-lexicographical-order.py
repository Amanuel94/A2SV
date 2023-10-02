class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # checks the number of strings < n with pref s
        if n == 1 and k == 1:
            return 1
        def search(s, n):
        
            r = len(s)
            k = len(str(n))
            m = k - r
            if m < 0:
                return 0
            if n == int(s):
                return 1
            ans = "1"*(k-r)
            if int(s) < int(str(n)[:r]):
                return int("1"+ans) if ans else 1
            if int(s) == int(str(n)[:r]):
                return int(ans)+int(str(n)[-m:])+1 if ans else int(str(n)[-m:])+1
            if int(s) >int(str(n)[:r]):
                return int(ans) if ans else 0

        N = 0
        ans = ""        
        for i in range(1, 10):
            nums = search(str(i), n)
            if N+nums > k-1:
                break
            if N+nums == k-1:
                return i+1
            N+=nums
        ans+=str(i)
        if int(ans) >= n:
            if N-k+1:
                    return int(ans[:-(N-k+1)])
            return int(ans)

        while True:
            for i in range(10):
                nums = search(ans + str(i), n)
                # print(nums, ans+str(i))
                if N+nums+1 > k-1:
                    break
                if N+nums+1 == k-1:
                    return int(ans+str(i+1))
                N+=(nums)
            ans+=str(i)
            N+=1
            if n == 10:
                print(N, k)
            if int(ans) >= n:
                # print("here", ans)
                if N-k+1:
                    return int(ans[:-(N-k+1)])
                return int(ans)