class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        for key in Counter(words):
            heap.append((-Counter(words)[key], key))

        heapify(heap)
        i = 0
        ans = []
        while i < k:
            ans.append(heappop(heap)[1])
            i+=1
        # print(ans)

        # l = r = 0
        # res = []
        # while temp < len(ans):
        #     if r < len(ans) and ans[l] == ans[r]:
        #         r+=1
        #     else:
        #         temp = l
        #         while temp != l:
        #             res.append()
                     


        return ans