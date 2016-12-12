"""283_Move_Zeroes.py."""


class Solution(object):
    """class."""

    def moveZeroes(self, nums):
        """:type nums: List[int].

        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            print (n)

list1 = [1, 0, 3, 0, 5]
c1 = Solution()
c1.moveZeroes(list1)
print (list1)
