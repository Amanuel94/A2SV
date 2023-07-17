class Solution:
    def numDecodings(self, s: str) -> int:

        """
        the number of ways to decode the s1 ... sn
        sum number of ways to decode s1 ... si , si+1.. sn valid
        
        """

        string = list(s)
        n = len(s)
        i = 1
        n_decode = [0]*n
        if string[0] != '0':
            n_decode[0] = 1
        while i < n:
            # print(n_decode)
            c = string[i]
            j = i-1
            while j >= 0:
                
                if int(c) > 26:
                    break
                
                if c[0] == '0':
                    c = string[j] + c
                    j-=1
                    continue
                else:
                    c = string[j] + c
                    n_decode[i]+= n_decode[j]
                j-=1
            if j==-1 and int(c)<= 26 and c[0]!='0':
                n_decode[i]+=1
            i+=1
        return n_decode[-1]