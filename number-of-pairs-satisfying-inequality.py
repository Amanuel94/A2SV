class Solution:
    def numberOfPairs(self, nums: List[int], nums2: List[int], diff: int) -> int:
        
        i = 0 
        while i < len(nums):
            nums[i]-=nums2[i]
            i+=1
        
        
        nums, count = self.mergeSort(nums, 0, len(nums)-1, diff)
    
        return count
    
    def mergeSort(self, nums, l, r, diff):
        
        if r - l == 0:
            return [nums[l]], 0
        
        mid = (r+l)//2
        
        left, count1 = self.mergeSort(nums, l, mid, diff)
        right, count2 =  self.mergeSort(nums, mid+1, r, diff)
        
        count =  count1+count2

        return self.merge(left, right, count, diff) 
        
    def merge(self, left, right, count, diff):
        # print(left, right, count)
        ans = []
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:

                ans.append(left[i])
                
                
                while k < len(right) and left[i]-diff > right[k]:
                    k+=1
                count+=len(right) - k
                
                
                i+=1
                
                    
            else:
                ans.append(right[j])
                
                
                
                j+=1
            
                
        while i < len(left):
            ans.append(left[i])
            while k < len(right) and left[i]-diff > right[k]:
                k+=1
            count+=len(right) - k
            i+=1
        while j < len(right):
            ans.append(right[j])
            j+=1
                
           
        
        return ans, count
        
        
