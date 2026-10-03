"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        tDict = {}

        for i in intervals:
            tDict[i.start] = tDict.get(i.start, 0) + 1
            tDict[i.end] = tDict.get(i.end, 0) - 1
        
        result = 0
        counter = 0

        for time in sorted(tDict.keys()):
            counter += tDict[time]
            result = max(result, counter)

        return result
