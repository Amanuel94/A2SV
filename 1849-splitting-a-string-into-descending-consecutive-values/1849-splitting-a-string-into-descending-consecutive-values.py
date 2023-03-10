class Solution:
    def splitString(self, s: str) -> bool:
        def can_split(start, last_num):
            if start == len(s):
                return True
            
            for end in range(start + 1, len(s) + 1):
                curr_num = int(s[start:end])
                
                if last_num - curr_num == 1 and can_split(end, curr_num):
                    return True
                
            return False
        
        for end in range(1, len(s)):
            first_num = int(s[:end])
            if can_split(end, first_num):
                return True
            
        return False
