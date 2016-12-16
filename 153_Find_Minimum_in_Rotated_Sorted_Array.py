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
            if nums[head] < nums[tail]:
                return nums[head]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[head] < nums[mid]:
                head = mid
            else:
                tail = mid - 1
        return [head]

# list1 = [2,3,4,5,1]
# print(list1)
# s = Solution()
# print (s.findMin(list1))
