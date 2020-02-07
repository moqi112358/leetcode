# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
#
#
# Note:
#
#
# 	You may assume that all inputs are consist of lowercase letters a-z.
# 	All inputs are guaranteed to be non-empty strings.
#
#


class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('')
        self.end = -1
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                node.children[c] = Node(c)
                node = node.children[c]
        node.children[self.end] = None
            
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        if self.end in node.children:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
