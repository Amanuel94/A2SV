class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = 0
    def insert(self, word: str) -> None:
        ptr = self.root
        for i, c in enumerate(word):
            c = ord(c)-97
            if ptr.children[c] is  None:
                ptr.children[c] = TrieNode()

            ptr = ptr.children[c]
        ptr.is_end = True
        ptr.count+=1

    def dfs(self, s, ptr, node):
        for i, nbr in enumerate(node.children):
            if nbr:
                c = chr(i+97)
                for j in range(ptr, len(s)):
                    if c == s[j]:
                        if nbr.is_end:
                            self.ans+=nbr.count
                        self.dfs(s, j+1, nbr)
                        break
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        trie = Trie()
        for word in words:
            trie.insert(word)
        trie.dfs(s, 0, trie.root)
        return trie.ans