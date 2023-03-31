class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        N = 10**9 + 7
        zipped = list(enumerate(instructions))
        
        inv = defaultdict(int)
        self.mergeSort(zipped, 0, len(zipped)-1, inv)
        counter = defaultdict(int)
        
        # print(inv)
        
        ans = 0
        # inv.sort(key= inv.get)
        # print(sorted(inv.items()))
        # for key in inv:
        #     print(inv[key], key)
        #     ans+= min(inv[key], key[0] - inv[key] - counter[key[1]])
        #     counter[key[1]]+=1
        
        inv = sorted(inv.items())
        
        counter[instructions[0]]+=1
        
        for key in inv:
            # print(key, key[1], key[0][0] -  key[1] - counter[key[0][1]], counter[key[0][1]])
            ans+= min(key[1], key[0][0] -  key[1] - counter[key[0][1]])
            ans%=N
            counter[key[0][1]]+=1
            
        
        
        return ans
        
        
    
    
    def mergeSort(self, tuples, left, right, inv):
        
        if right == left:
            return [tuples[left]]
        
        mid =  (left + right)//2
        
        left_sorted = self.mergeSort(tuples, left, mid, inv)
        right_sorted = self.mergeSort(tuples, mid+1, right, inv)
        
        
        return self.merge(left_sorted, right_sorted, inv)
    
    
    def merge(self, left, right, inv):
        
        i = j  = 0
        k = 0
        ans = []
        while i < len(left) and j < len(right):
            if left[i][1] <= right[j][1]:
                ans.append(left[i])
                
                
                
                i+=1
            else:
                ans.append(right[j])
                
                # while k > -1 and left[k][1] > right[j][1]:
                #     k-=1
                
                # while k < len(ans) a
                
                inv[right[j]]+= len(left) - i
                
                
                j+=1
                
        while i <len(left):
            ans.append(left[i])
            # while k < len(right) and right[k][1] < left[i][1]:
            #     k+=1
            # inv[left[i]]+= j
            i+=1
        
        while j <len(right):
            ans.append(right[j])
            inv[right[j]]+=len(left) - i
            j+=1
            
        return ans
        
