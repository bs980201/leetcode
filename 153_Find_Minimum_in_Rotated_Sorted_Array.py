"""153_Find_Minimum_in_Rotated_Sorted_Array.py."""


class Solution(object):
    """Class."""

    def findMin(self, nums):
        """
        :type nums: List[int].

        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        head = 0
        tail = n - 1

        while head != tail:
            mid = (head + tail) // 2 + 1
            # 如果整個數列是順的也就是[1,2,3,4,5] 那就直接return 1就好
            if nums[head] < nums[tail]:
                return nums[head]
            # 如果中間的mid跟mid-1 是順向，那就代表mid就是最小值 e.g:[4,5,1,2,3]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            # 接下來只剩下[2,3,4,5,1],[3,4,5,1,2], [5,1,2,3,4]這三種可能
            # 發現，1都在非順向的那區，也就是[4,5,1],[5,1,2],[5,1]
            # 所以我們只要確認某一區是否順向，是順向的話，就直接找另外一區的就好
            # 不是順向的話，就繼續在這個區尋找！
            if nums[head] < nums[mid]:
                head = mid
            else:
                tail = mid - 1
        return [head]

# list1 = [2,3,4,5,1]
# print(list1)
# s = Solution()
# print (s.findMin(list1))
