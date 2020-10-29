# Implement the RandomizedSet class:
#
#
# 	bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# 	bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# 	int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
#
#
# Follow up: Could you implement the functions of the class with each function works in average O(1) time?
#
#  
# Example 1:
#
#
# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]
#
# Explanation
# RandomizedSet randomizedSet = new RandomizedSet();
# randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
# randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
# randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
# randomizedSet.insert(2); // 2 was already in the set, so return false.
# randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
#
#
#  
# Constraints:
#
#
# 	-231 <= val <= 231 - 1
# 	At most 105 calls will be made to insert, remove, and getRandom.
# 	There will be at least one element in the data structure when getRandom is called.
#
#


# import random
# class RandomizedSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = set()
        

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.data:
#             self.data.add(val)
#             return True
#         else:
#             return False
        

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.data:
#             self.data.remove(val)
#             return True
#         else:
#             return False
        

#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         return random.choice(list(self.data)) # set to list waste of tume

from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
