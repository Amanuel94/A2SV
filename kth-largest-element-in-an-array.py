class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(nums, l, r, k):
            if r - l == 0:
                return nums[-k]
            elif r -l == 1:
                nums[l], nums[r] = min(nums[l], nums[r]), max(nums[l], nums[r])
                return nums[-k]
            
            write = l
            read = l+1
            
            while read <= r:
                
                if nums[read] <= nums[l]:
                    write+=1
                    nums[read], nums[write] = nums[write], nums[read]
                read+=1
                
            pos =  len(nums) - k
            # print(nums, l, r, write)
            nums[l], nums[write] = nums[write], nums[l]
            if pos == write:
                return nums[write]
            elif pos > write:
                return quickSelect(nums, write+1, r, k)
            else:
                return quickSelect(nums, l, write-1, k)
            
            
        return quickSelect(nums, 0, len(nums)-1,k)
            
                
                
                
                
    '''
    
    3 2 1 5 6 4
    
    3 1 2 5 6 4
    
    '''
                
        
