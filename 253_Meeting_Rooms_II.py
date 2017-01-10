"""253_Meeting_Rooms_II.py."""
import collections
# Definition for an interval.


class Interval(object):
    """Interval."""

    def __init__(self, s=0, e=0):
        """init."""
        self.start = s
        self.end = e


class Solution(object):
    """solution."""

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval].

        :rtype: int
        """
        # Solution 1
        dict_time_to_rooms = collections.defaultdict(int)
        # 以每個開始時間點與結尾的時間點作為key, 碰到如果是開始，就把對應的value+1，是結束就把對應value-1
        # 這樣就可以知道該時間點到底要多開幾間房間或是再關幾間房間
        for i in intervals:
            dict_time_to_rooms[i[0]] += 1
            dict_time_to_rooms[i[1]] -= 1
        sum_room, ans = 0, 0
        # 當創立上述的dict之後，就可以按照時間順序把房間開開關關，從這開開關關的過程中可以把max房間數記起來得解
        for time in sorted(dict_time_to_rooms):
            sum_room += dict_time_to_rooms[time]
            ans = max(ans, sum_room)
        return ans

        # Solution 2
        ans = 0
        endtime = []
        # 這方法是依照每個時段來檢查最大的重複時段，也就是最大房間需求量
        # 先把房間依照預約的開始時間sort好，因為我們要利用開始時間跟其他時段的結尾時間來檢查重疊
        for i in sorted(intervals, key=lambda i: i[0]):
            endtime = [e for e in endtime if i[0] < e]
            endtime.append(i[1])
            ans = max(len(endtime), ans)
        return ans


s = Solution()
list1 = [[5, 10], [0, 30], [15, 20]]
list2 = [[2, 7]]
list3 = [[13, 15], [1, 13]]
print (s.minMeetingRooms(list1))
