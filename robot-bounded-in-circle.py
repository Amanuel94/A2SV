class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        v = (0,0)
        d = (0, 1)
        for i in instructions:
            if i == "G":
                v = (v[0]+d[0], v[1]+d[1])
            if i == "L":
                d = (-d[1], d[0])
            if i == "R":
                d = (d[1], -d[0])
            print(v)
        return v == (0,0) or d != (0, 1)