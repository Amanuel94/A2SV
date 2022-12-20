class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i+1 and nums1[i] > nums2[j]:
                nums1[k], nums1[i] = nums1[i], 0
                i-=1
                k-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1         
         
