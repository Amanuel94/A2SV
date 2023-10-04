class TrieNode:
    def __init__(self):
        self.children = [None]*27
        self.index = -1
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, ind):
        ptr = self.root
        ptr.index = ind
        for c in word:
            idx = ord(c) - ord('a')
            if ptr.children[idx] is None:
                ptr.children[idx] = TrieNode()
            ptr = ptr.children[idx]
            ptr.index = ind

    def search(self, word):
        ptr = self.root
        i = 0
        while i < len(word):
            idx = ord(word[i]) - ord('a')
            ptr = ptr.children[idx]
            if ptr is None:
                return -1
            i+=1
        return ptr.index


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for j, word in enumerate(words):
            for i in range(len(word)):
                self.trie.insert(word[i:]+'{'+word, j)

    def f(self, pref: str, suff: str) -> int:

        return self.trie.search(suff+'{'+pref)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)