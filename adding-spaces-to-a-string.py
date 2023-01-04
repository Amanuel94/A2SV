class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        string = []
        cur_ind = 0
        val = spaces[cur_ind]
        i = 0
        for index in range(len(s)):

            if index == val:
                 string.append(" ")
                 string.append(s[index])
                 cur_ind+=1
                 val = spaces[cur_ind] if cur_ind < len(spaces) else 0

            else:

                string.append(s[index])

            if cur_ind == len(spaces):
                i = index
                break

        return "".join(string) + s[i+1:]
