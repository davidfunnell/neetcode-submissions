"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetingDict = {}

        for i in intervals:
            meetingDict[i.start] = meetingDict.get(i.start, 0) + 1
            meetingDict[i.end] = meetingDict.get(i.end, 0) - 1
        
        rooms = 0
        temp = 0
        for meeting in sorted(meetingDict.keys()):
            temp += meetingDict[meeting]
            rooms = max(rooms, temp)
        
        return rooms