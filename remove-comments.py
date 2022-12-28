class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """

        uncommented = ""

        code  = "\|".join(source)
        
        i = 0
        while i < len(code):

            while i < len(code)-1 and (code[i:i+2] != "/*" and code[i:i+2] != "//"):
                uncommented+=code[i]
                i+=1

            if i < len(code)-1 and code[i:i+2] == "/*":
                i = i + 2 + code[i+2:].index("*/") + 2

            elif i < len(code)-1 and code[i:i+2] == "//":

                if "\|" in code[i+2:]:
                    i = i + 2 + code[i+2:].index("\|")

                else:
                    i = len(code)

            if i == len(code)-1:
                uncommented += code[i]
                break

        uncommented  =  [i for i in uncommented.split('\|') if i != ""]

        return uncommented


            


        

                

             


                    

