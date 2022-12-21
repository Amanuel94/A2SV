class Solution(object):
    def interpret(self, command):
        out = prev =  ""
        for i in command:
            if i == 'G':
                out+='G'
            elif i == ')' and prev == '(':
                out+='o'
            elif i == ')' and prev == 'l':
                out+='al'
            else:
                prev = i
        return out
