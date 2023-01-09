class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = num1.split('+')
        num2 = num2.split('+')

        real_product = eval("("+ num1[0] + ")*(" + num2[0] + ")-(" + num1[1][:-1]  + ")*(" + num2[1][:-1]+ ")") 
        imaginary_product = eval("("+ num1[0] + ")*(" + num2[1][:-1] + ")+(" + num1[1][:-1]  + ")*(" + num2[0]+ ")") 

        return str(real_product) + "+" +str(imaginary_product)+"i"
