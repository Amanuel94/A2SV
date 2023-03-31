class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = list(Counter(nums).items())
        
        modes = self.quickSelect(0, len(frequency)-1, k, frequency)
        
        return [mode[0] for mode in modes]
        
        
    def quickSelect(self, left, right, k, freq):
        # print(freq, left, right)
        n_uniques = len(freq)
        if right-left+1 <= 1:
            return freq[n_uniques - k:]
        
        write = left
        read = left+1
        
        while read <= right:
            
            if freq[read][1] < freq[left][1]:
                write+=1
                freq[read], freq[write]= freq[write], freq[read]
                
            read+=1
        freq[write], freq[left] = freq[left], freq[write]
        
        if write == n_uniques - k:
            return freq[n_uniques - k:]
        elif write < n_uniques - k:
            return self.quickSelect(write+1, right, k, freq)
        else:
            return self.quickSelect(left, write-1, k, freq)
