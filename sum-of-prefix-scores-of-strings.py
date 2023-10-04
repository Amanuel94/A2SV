class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    
    def insert(self, word):
        ptr = self.root
        for i, c in enumerate(word):
            idx = ord(c) - ord('a')
            if ptr.children[idx] is None:
                ptr.children[idx] = TrieNode()
            ptr = ptr.children[idx]
            ptr.count+=1
        # print(ptr.count)

    def findSumOfScore(self, word):
        ptr = self.root
        # print(word)
        ans = 0
        for c in word:
            ptr = ptr.children[ord(c)-ord('a')]
            ans+=ptr.count
        return ans
    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.findSumOfScore(word))

        return ans