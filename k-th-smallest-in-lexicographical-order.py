class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # checks the number of strings < n with prefix 'prefix'

        def search(prefix, n):
        
            pref_len = len(prefix)
            n_len = len(str(n))
            len_diff = n_len - pref_len
            if len_diff < 0:
                return 0
            if n == int(prefix):
                return 1

            ans = "1"*(len_diff)
            if int(prefix) < int(str(n)[:pref_len]):
                return int("1"+ans) 
            if int(prefix) == int(str(n)[:pref_len]):
                return int(ans)+int(str(n)[-len_diff:])+1 if ans else int(str(n)[-len_diff:])+1 
            if int(prefix) >int(str(n)[:pref_len]):
                return int(ans) if ans else 0

        smaller_nums = 0
        ans = ""        
        for i in range(1, 10):
            nums = search(str(i), n)
            if smaller_nums+nums > k-1:
                break
            if smaller_nums+nums == k-1:
                return i+1
            smaller_nums+=nums
        ans+=str(i)
        if int(ans) >= n:
            if smaller_nums-k+1:
                    return int(ans[:-(smaller_nums-k+1)])
            return int(ans)

        while True:
            for i in range(10):
                nums = search(ans + str(i), n)
                # print(nums, ans+str(i))
                if smaller_nums+nums+1 > k-1:
                    break
                if smaller_nums+nums+1 == k-1:
                    return int(ans+str(i+1))
                smaller_nums+=(nums)
            ans+=str(i)
            smaller_nums+=1
            if n == 10:
                print(smaller_nums, k)
            if int(ans) >= n:
                if smaller_nums-k+1:
                    return int(ans[:-(smaller_nums-k+1)])
                return int(ans)