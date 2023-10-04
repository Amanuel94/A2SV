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

    def withPrefix(self, word:str):
        ptr = self.root
        i = 0
        pre = word
        while ptr and i < len(word):
            ptr = ptr.children[ord(word[i]) - 97]
            i+=1
        keys = []
        def dfs(node, cur):
                
            if node and node.is_end:
                keys.append(cur)
            
            for i, nbr in enumerate(node.children):
                if nbr is not None:
                    dfs(nbr, cur+chr(i+97))
        if ptr is not None:
            dfs(ptr, word)
        return keys

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class MapSum:

    def __init__(self):

        self.dict = {}
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.dict[key] = val
        self.trie.insert(key)
        

    def sum(self, prefix: str) -> int:
        ans = 0
        for key in self.trie.withPrefix(prefix):
            ans+= self.dict[key]
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)