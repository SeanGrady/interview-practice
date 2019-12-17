from typing import List
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_meetings = sorted(intervals, key=lambda meeting: meeting[0])
        endtime_queue = []
        max_rooms = 0
        for meeting in sorted_meetings:
            meeting_start = meeting[0]
            meeting_end = meeting[1]
            if not endtime_queue or (meeting_start < endtime_queue[0]):
                heappush(endtime_queue, meeting_end)
            else:
                while endtime_queue and meeting_start >= endtime_queue[0]:
                    heappop(endtime_queue)
                heappush(endtime_queue, meeting_end)
            concurrent_rooms = len(endtime_queue)
            max_rooms = max(concurrent_rooms, max_rooms)
        return max_rooms
