# -*- coding:utf-8 -*-


# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
#
# 	WordDictionary() Initializes the object.
# 	void addWord(word) Adds word to the data structure, it can be matched later.
# 	bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
#  
# Example:
#
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
#  
# Constraints:
#
#
# 	1 <= word.length <= 500
# 	word in addWord consists lower-case English letters.
# 	word in search consist of  '.' or lower-case English letters.
# 	At most 50000 calls will be made to addWord and search.
#
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
