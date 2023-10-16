class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        s = s.replace('-', '+-')
        s = s.split('+')
        ans = 0
        for term in s:
            term = term.strip()
            cur = []
            factor = []
            for i in range(len(term)):
                if term[i] == ' ':
                    continue
                if term[i] in "0123456789-":
                    factor.append(term[i])
                if term[i] in '*/':
                    cur_term = int("".join(factor))
                    factor = []
                    if len(cur) == 2:
                        op = cur.pop()
                        prev_term = cur.pop()
                        if op == "*":
                            cur.append(prev_term * cur_term)
                        else:
                            cur.append(int(str(prev_term/cur_term).split('.')[0]))
                    else:
                        cur.append(cur_term)
                    cur.append(term[i])

            cur_term = int("".join(factor))
            if len(cur) == 2:
                op = cur.pop()
                prev_term = cur.pop()
                if op == "*":
                    cur_term = prev_term * cur_term
                else:
                    cur_term = int(str(prev_term/cur_term).split('.')[0])
            
            ans+=cur_term
        return ans