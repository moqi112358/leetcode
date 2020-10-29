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


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie;
        for i in word:
            if i in node:
                node = node[i]
            else:
                node[i] = {}
                node = node[i]
        node['end'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for i in word:
            if i in node:
                node = node[i]
            else:
                return False
        if 'end' in node:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for i in prefix:
            if i in node:
                node = node[i]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
