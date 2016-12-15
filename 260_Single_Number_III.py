"""260_Single_Number_III.py."""


class Solution(object):
    """class."""

    def singleNumber(self, nums):
        """:type nums: List[int].

        :rtype: List[int]
        """
        result = 0
        for num in nums:
            result ^= num

        position = 1

        while result & position == 0:
            position = position << 1

        ans = [0, 0]
        for num in nums:
            if num & position == 0:
                ans[0] ^= num
            else:
                ans[1] ^= num

        return ans

list1 = [5, 6, 10, 10, 3, 3]

instance = Solution()
result = instance.singleNumber(list1)
print (result)
