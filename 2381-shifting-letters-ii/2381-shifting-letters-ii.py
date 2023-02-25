class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        
        shift_arr = [0]*len(s)
        
        for shift in shifts:
            shift_arr[shift[0]]+=2*shift[-1]-1
            if shift[1]+1 < len(s):
                shift_arr[shift[1]+1]-=2*shift[-1]-1
            
        i = 1
        while i < len(s):
            shift_arr[i] = shift_arr[i-1]+shift_arr[i]
            i+=1
        
        ans = ""    
        for i, net in enumerate(shift_arr):
            ans = ans + chr((ord(s[i]) + net - 97)%26 + 97)
        return ans
            
            
        
        