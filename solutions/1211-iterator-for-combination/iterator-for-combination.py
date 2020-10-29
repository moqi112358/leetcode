# Design an Iterator class, which has:
#
#
# 	A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# 	A function next() that returns the next combination of length combinationLength in lexicographical order.
# 	A function hasNext() that returns True if and only if there exists a next combination.
#
#
#  
#
# Example:
#
#
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.
#
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
#
#
#  
# Constraints:
#
#
# 	1 <= combinationLength <= characters.length <= 15
# 	There will be at most 10^4 function calls per test.
# 	It's guaranteed that all calls of the function next are valid.
#
#


class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        n, k = len(characters), combinationLength
        
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:  
                self.combinations.append(''.join(curr[:]))
                # speed up by non-constructing combinations 
                # with more than k elements
                return 
            for i in range(first, n):
                # add i into the current combination
                curr.append(characters[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()

        backtrack()
        self.combinations.reverse()
        
    def next(self) -> str:
        return self.combinations.pop()

    def hasNext(self) -> bool:
        return self.combinations
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
