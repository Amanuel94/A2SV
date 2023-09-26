class TrieNode:

    def __init__(self):
        self.children =[None]*26
        self.is_end = False

class WordDictionary:

    def __init__(self):

        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:

        ptr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if ptr.children[idx] is None:
                ptr.children[idx] = TrieNode()
            ptr = ptr.children[idx]
        ptr.is_end = True
        

    def search(self, word: str, root = None, is_end = True) -> bool:


        if root is None:
            root = self.root

        if word == "":
            return is_end

        if word[0] == ".":
            for i, nbr in enumerate(root.children):
                if nbr is not None:
                    if self.search(word[1:], nbr, nbr.is_end):
                        return True
        else:
            
            c = ord(word[0]) - ord('a')
            return root.children[c] and self.search(word[1:], root.children[c], root.children[c].is_end)
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)