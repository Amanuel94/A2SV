class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        ptr = self.root
        for i, c in enumerate(word):
            c = ord(c)-97
            if ptr.children[c] is  None:
                ptr.children[c] = TrieNode()

            ptr = ptr.children[c]
        ptr.is_end = True
    
    def longestDictWord(self, node):
        
        # if not node.is_end:
        #     return ""
        
        max_str = ""
        max_len = 0

        for i, nbr in enumerate(node.children):
            if nbr is not None and nbr.is_end:
                word = chr(i+97) + self.longestDictWord(nbr)
                if len(word) > max_len:
                    max_len = len(word)
                    max_str = word
                elif len(word) == max_len and word < max_str:
                    max_str = word
        return max_str

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        trie.root.is_end = True

        return  trie.longestDictWord(trie.root)