class Solution:
    def minimumOperations(self, nums: List[int]) -> int:


        n = len(nums)
        if n == 1:
            return 0
        even_indices = Counter([nums[i] for i in range(n) if i%2 == 0])
        odd_indices = Counter([nums[i] for i in range(n) if i%2])
    
        even_indices = sorted(even_indices.items(), key = lambda k:k[1], reverse= True)
        odd_indices = sorted(odd_indices.items(), key = lambda k:k[1], reverse= True)

        if even_indices[0][0] !=  odd_indices[0][0]:
            return n//2+(n%2) - even_indices[0][1] + n//2 - odd_indices[0][1]
        
        even_indices.append((-1, 0))
        odd_indices.append((-1, 0))
     
        # print(even_indices, odd_indices)
        return min(
            n//2+(n%2) - even_indices[0][1] + n//2 - odd_indices[1][1],
            n//2+(n%2) - even_indices[1][1] + n//2 - odd_indices[0][1]
        )