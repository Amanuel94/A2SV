class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        
        def isValidIp(parts):
            
            for part in parts:
                if not part or int(part) > 255 or (len(part) > 1 and part[0] == '0'):
                    return False
                
            return True
        
        def make_ips(depth, parts):
            nonlocal ips
            
            if depth == 4:
                
                if isValidIp(parts):
                    ips.append('.'.join(parts))
                    
                return 
            
            last = parts.pop()
            i  = 1
            while i < len(last):
                parts.append(last[:i])
                parts.append(last[i:])
                
                make_ips(depth+1, parts)
                
                parts.pop()
                parts.pop()
                i+=1
            parts.append(last)
                
                
        make_ips(1, [s])
        
        return ips
    
    
        '''
        255 255 111 35
        '''
                    
  
