class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root 

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.end_of_word = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)

        result = ""
        current = trie.root
        while len(current.children) == 1 and current.end_of_word == False:
            char, node = next(iter(current.children.items()))
            result += char
            current = node

        return result