class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:   

        """
        one of the following
            do nothing if bill is 5
            take and return 5
            take and return 10 + 5 or 5+5+5
        """
        state = [0,0,0]
        for bill in bills:
            print(state, bill)
            if bill == 5:
                state[0]+=1
            elif bill == 10 and state[0] > 0:
                state[1]+=1
                state[0]-=1
            elif bill == 10 and state[0] < 1:
                return False
            elif bill == 20:
                if state[1] > 0 and state[0]>0:
                    state[0]-=1
                    state[1]-=1
                elif state[0]>=3:
                    state[0]-=3
                else:
                    return False
                state[2]+=1
        return True