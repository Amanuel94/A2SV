class Solution(object):
    def freqAlphabets(self, s):
        
        out = ""
        s_ = s.split('#')
        
        for chars in s_[:-1]:
            i = 0
            
            while i < len(chars):
                if i < len(chars)-2:
                    out += str(chr(int(chars[i])+96))
                    i+=1
                else:
                    out+= str(chr(int(chars[i:len(chars)])+96))
                    i+=2
                
        if s_[-1]:
            for c in s_[-1]:
                out += str(chr(int(c)+96))

        return out
