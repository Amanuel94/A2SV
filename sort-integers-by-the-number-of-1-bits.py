class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # print([(i, i.bit_count() )for i in arr])
        return sorted(arr, key = lambda x: (x.bit_count(), x) )