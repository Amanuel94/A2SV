class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        words = list(map(Counter, words))

        ans =[]
    
        for key in words[0].keys():
            min_ = words[0][key]
            for word in words[1:]:
                    min_ = min(min_, word.get(key, 0))
            ans.extend([key]*min_)


        return ans
        

            

        
