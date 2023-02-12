class Solution(object):
    def numberToWords(self, num):
        s =  self.toWords(num, 0)
        t = ""
        i = 1
        while i < len(s)-1:
            if ord(s[i+1]) < 97:
                s = s[:i+1] + " " + s[i+1:]
                i+=1
            i+=1
            
        return s
                
        
    
    def toWords(self, num, c):
        if num == 0 and c != 0:
            return ""
        elif num == 0 and c == 0:
            return "Zero"
        else:
            chunk_names = ["Thousand", "Million", "Billion"]
            word  = ""
            ones = {"1":"One", "2":"Two", "3":"Three", "4":"Four", "5":"Five", "6":"Six", "7":"Seven", "8":"Eight", "9":"Nine"}
            tens = {"2":"Twenty", "3":"Thirty", "4":"Forty", "5":"Fifty", "6":"Sixty", "7":"Seventy", "8":"Eighty", "9":"Ninety"}
            teens = {"10": "Ten", "11": "Eleven", "12":"Twelve", "13":"Thirteen", "14":"Fourteen", "15":"Fifteen", "16":"Sixteen", "17":"Seventeen", "18":"Eighteen", "19":"Nineteen"}
            n = str(num%1000)
            dig = len(n)
            if dig == 3:
                word = word + ones[n[0]] + "Hundred"
                if n[1]!= "0" and n[1]!= "1":
                    word = word + "" + tens[n[1]]
                    if n[2]!= "0":
                        word = word + "" + ones[n[2]]
                elif n[1] == "0":
                    if n[2]!= "0":
                        word = word + "" + ones[n[2]]
                else:
                    word =  word + "" + teens[n[1:]]
            elif dig == 2:
                if n[0]!= "1":
                    word = word + tens[n[0]]
                    if n[1]!= "0":
                        word = word + "" + ones[n[1]]
                elif n[0] == "1":
                    word =  word + teens[n]
            elif dig == 1 and n != "0":
                word = word + ones[n]
            if num//1000 == 0 or (num//1000)%1000 == 0:
                s = ""
            else:
                if num%1000 != 0:
                    s = chunk_names[c] + ""
                else:
                    s = chunk_names[c]
            c+=1


            return self.toWords(num//1000, c) + s + word