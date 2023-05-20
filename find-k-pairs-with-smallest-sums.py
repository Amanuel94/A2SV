class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        i = 0
        
        while i < len(nums1):
            j = 0
            while j < len(nums2):
                n1, n2 = nums1[i], nums2[j]
                heappush(heap, (-n1-n2, -n1, -n2))
                if len(heap) == k:
                    break
                j+=1
            if len(heap) == k:
                    break
            i+=1
        while j < len(nums2) and -heap[0][0] > nums1[i] + nums2[j]:
            j+=1
            heappop(heap)
            heappush(heap, (-nums1[i]-nums2[j], -nums1[i], -nums2[j]))
            


        ii = i+1
        # j = len(nums2)
        while ii < len(nums1):
            jj = 0
            while jj < j:
                if -heap[0][0] > nums1[ii] + nums2[jj]:
                    heappop(heap)
                    heappush(heap, (-nums1[ii]-nums2[jj], -nums1[ii], -nums2[jj]))
                else:
                    j = jj
                    break
                jj+=1
            ii+=1
        ans = []
        for sum_, x, y in heap:
            ans.append([-x, -y])
        return sorted(ans)