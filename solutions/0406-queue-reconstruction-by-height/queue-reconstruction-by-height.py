# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#  
#
# Example
#
#
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
#
#  
#


class Solution:
    # Method 1: From low to high
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    #     sorted_people = sorted(people, key = lambda x: (x[0], x[1]))
    #     res = [None] * len(people)
    #     for i in range(len(sorted_people)):
    #         (value, index) = sorted_people[i]
    #         count = 0
    #         for pos in range(len(res)):
    #             if count == index and res[pos] is None:
    #                 break
    #             if res[pos] is None or res[pos][0] >= value:
    #                 count += 1
    #         res[pos] = sorted_people[i]
    #     return res
    
    # Method 2: From high to low
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in sorted_people:
            res.insert(p[1], p)
        return res

