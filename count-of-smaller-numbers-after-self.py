class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ref = defaultdict(int)
        packed = list(enumerate(nums))
        self.mergeSort(packed, 0,len(nums)-1, ref)
        # print(ref)
        
        i = 0 
        while i < len(nums):
            nums[i] = ref[(i, nums[i])]
            i+=1
        return nums
        
    def mergeSort(self, nums, l, r, d):
        
        if r-l+1 == 1:
            return [nums[l]]
        
        mid =  (l+r)//2
        
        left = self.mergeSort(nums, l, mid, d)
        right = self.mergeSort(nums, mid+1, r, d)
        
        return self.merge(left, right, d)
    
    def merge(self, left, right, d):
        ans = []
        i = j = 0
        while i < len(left) and j < len(right):
            
            if left[i][1]<=right[j][1]:
                ans.append(left[i])
                d[left[i]]+=j
                i+=1
                
                
            else:
                ans.append(right[j])
                # d[right[j]]+=i
                j+=1
                
        while i < len(left):
            ans.append(left[i])
            d[left[i]]+=j
            i+=1
        while j < len(right):
            ans.append(right[j])
            # d[right[j]]+=i
            j+=1
                
        return ans
            
           
        
        
    """
    5 2 6 1
    
    2 5 1 6
    
    1 2 5 6
    
    
    
    
    """
        
