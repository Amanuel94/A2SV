class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        p = {chr(i):chr(i) for i in range(97, 97+26)}

        def getP(c):
            if p[c] == c:
                return c
            p[c] = getP(p[c])
            return p[c]
        inequ = list(filter(lambda x:x[1]=='!', equations))
        for equation in equations:
            x, op, y = equation[0], equation[1], equation[3] 
            if op != '!':
                par_x, par_y = getP(x), getP(y)
                p[par_x] = par_y
        for equation in inequ:
            x, op, y = equation[0], equation[1], equation[3] 
            par_x, par_y = getP(x), getP(y)
            if par_y == par_x:
                return False
                # p[par_x] = par_y
        return True