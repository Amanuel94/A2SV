class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # Helper function to count numbers with specific prefix
        def countNumbersWithPrefix(prefix, n):
            pref_len = len(prefix)
            n_len = len(str(n))
            len_diff = n_len - pref_len

            if len_diff < 0:
                return 0

            # If prefix equals n, return 1
            if n == int(prefix):
                return 1

            # Calculate the count of numbers with the given prefix
            count = "1" * (len_diff)
            if int(prefix) < int(str(n)[:pref_len]):
                return int("1" + count)
            elif int(prefix) == int(str(n)[:pref_len]):
                return int(count) + int(str(n)[-len_diff:]) + 1 if count else int(str(n)[-len_diff:]) + 1
            else:
                return int(count) if count else 0

        smaller_nums = 0
        ans = ""

        # Loop through prefixes (1 to 9) to find the kth number
        for i in range(1, 10):
            nums = countNumbersWithPrefix(str(i), n)
            # If current prefix contains the kth number
            if smaller_nums + nums > k - 1:
                break
            # If kth number is in the next prefix
            if smaller_nums + nums == k - 1:
                return i + 1
            smaller_nums += nums

        ans += str(i)

        # Handle edge case when kth number exceeds n
        if int(ans) >= n:
            if smaller_nums - k + 1:
                return int(ans[:-(smaller_nums - k + 1)])
            return int(ans)

        # Loop through prefixes and find the kth number
        while True:
            for i in range(10):
                nums = countNumbersWithPrefix(ans + str(i), n)
                # If current prefix contains the kth number
                if smaller_nums + nums + 1 > k - 1:
                    break
                # If kth number is in the next prefix
                if smaller_nums + nums + 1 == k - 1:
                    return int(ans + str(i + 1))
                smaller_nums += nums
            ans += str(i)
            smaller_nums += 1

            # Handle edge case when kth number exceeds n
            if int(ans) >= n:
                if smaller_nums - k + 1:
                    return int(ans[:-(smaller_nums - k + 1)])
                return int(ans)