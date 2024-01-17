class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()


newTrie = Trie(1)
print(newTrie)