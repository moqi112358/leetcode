# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
#
# Example 2:
#
#
# Input: [[7,10],[2,4]]
# Output: 1
#
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
#


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        res = []
        intervals = sorted(intervals, key = lambda x: x[0] )
        heapq.heappush(res, intervals[0][1])
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= res[0]:
                heapq.heappop(res)
            heapq.heappush(res, interval[1])
        return len(res)
