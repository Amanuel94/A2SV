class Solution(object):
    def similarPairs(self, words):
        count =  0
        def isSimilar(a , b):
            for i in a:
                if i not in b:
                    return False
            for i in b:
                if i not in a:
                    return False

            return True

        i = 0
        while words:
            j = i+1
            n = 1
            arr = []
            while j < len(words):
                if isSimilar(words[i], words[j]):
                    n+=1
                else:
                    arr.append(words[j])
                j+=1
            count+= ((n)*(n-1))/2
            words = arr
    
        return count
