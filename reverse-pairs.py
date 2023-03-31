class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        nums, count = self.mergeSort(nums, 0, len(nums)-1)
    
        return count
    
    def mergeSort(self, nums, l, r):
        
        if r - l == 0:
            return [nums[l]], 0
        
        mid = (r+l)//2
        
        left, count1 = self.mergeSort(nums, l, mid)
        right, count2 =  self.mergeSort(nums, mid+1, r)
        
        count =  count1+count2

        return self.merge(left, right, count) 
        
    def merge(self, left, right, count):
        # print(left, right, count)
        ans = []
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:

                ans.append(left[i])
                
                while k < len(right) and left[i] > 2*right[k]:
                    k+=1
                count+=k
                i+=1
                
                    
            else:
                ans.append(right[j])
                j+=1
            
                
        while i < len(left):
            ans.append(left[i])
            while k < len(right) and left[i] > 2*right[k]:
                k+=1
            count+=k
            i+=1
        while j < len(right):
            ans.append(right[j])
            j+=1
        
        return ans, count    
        
        
