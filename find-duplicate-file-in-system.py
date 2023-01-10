class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """

        p = {}
        d = {}

        for path in paths:

            files = path.split()
            p[files[0]] = files[1:]

        for key in p.keys():
            for txt in p[key]:
                if d.get(txt[txt.find('(')+1: -1], False):
                    d[txt[txt.find('(')+1: -1]].append(key + "/"+txt[:txt.find('(')])
                else:
                    d[txt[txt.find('(')+1: -1]] = [key+ "/"+txt[:txt.find('(')]]
        ans = []
        for k in d.keys():
            s = []
            if len(d[k]) > 1:
                for txt in d[k]:
                    s.append(txt)
                ans.append(s)

            
        return ans
