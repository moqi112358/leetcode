# -*- coding:utf-8 -*-


# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.dict = collections.defaultdict(list)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.dict[len(word)].append(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if '.' not in word:
            return word in self.dict[len(word)]
        for w in self.dict[len(word)]:
            if self.match(w, word):
                return True
        return False
    
    def match(self, w, pattern):
        for i in range(len(pattern)):
            if pattern[i] == '.':
                continue
            else:
                if pattern[i] != w[i]:
                    return False
        return True
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
