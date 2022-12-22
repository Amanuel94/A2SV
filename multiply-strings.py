class Solution(object):
    def multiply(self, num1, num2):
        # declare where we put our string product
        res = ""
        #here we reverse our num2 for computational purposes
        num2 = num2[::-1]

        # declare the sizes as variables
        n1 = len(num1)
        n2 = len(num2)

        # declare our product list
        prods = []

        i = 0
        # multiply by each digit of num2 and store our partial products in our product list
        while i < n2:

            res = self.mul(num1, num2[i], n1)

            # add zeros at the end to make for the shifts
            res =  res + "0"*(i)
            prods.append(res)
            i+=1

        # then we sum over our prod list to get our answer

        out = prods[0]
        for i in prods[1:]:
            out = self.add(i, out)
        # if out is a bunch of zeros, like '0000' then we just need our function to return '0'
        for i in out:
            if int(i):
                return out

        return "0"



    def add(self, num1, num2):
        # declare two pointers 
        i = len(num1)-1
        j = len(num2)-1
        
        # if num1 is longer
        if i >= j:

            #declare sum and carry variables
            carry = 0
            sum_ = ""

            # add the corresponding digits of num1 and num2
            while j >=0:

                temp_sum = int(num1[i]) + int(num2[j]) + carry
                sum_ = str(temp_sum%10) + sum_ # add the unit digit of the sum to our sum_ variable
                carry = temp_sum // 10 # add the tenth digit of our sum to our carry variable

                i-=1
                j-=1

            # add the remaining carry bit to  remaining digits of num1 since it is longer than num2
            while i>=0:

                temp_sum = int(num1[i]) + carry
                sum_ = str(temp_sum%10) + sum_
                carry = temp_sum // 10

                i-=1

            # if there still is a carry, add it to the front of our result
            if carry:
                sum_ = str(carry) + sum_

            return sum_

        else:
            # if num2 is longer swap num2 and num1, and reevaluate the function
            return  self.add(num2, num1)

 

    def mul(self, num1, k, n):

        #declare the variables where we save the product and the carry
        carry = 0
        prod = 0
        res = ""

        i  = n -1

        while i > -1:

            prod = int(num1[i])*int(k) + carry
            res = str(prod%10) + res # save the unit digit of the product to our prod variable
            carry = prod // 10 # save the tenth digit of our product to our carry variable
            i-=1
        
        # if there is a carry add it to the front, else return the result
        return str(carry) + res if carry else res 
