"""283_Move_Zeroes.py."""


class Solution(object):
    """class."""

    def moveZeroes(self, nums):
        """:type nums: List[int].

        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # solution1
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                nums.append(nums.pop(i))

        # solution2
        # position = 0
        # for i, num in enumerate(nums):
        #     if num != 0:
        #         nums[position], nums[i] = nums[i], nums[position]
        #         position += 1


# list1 = [5,3,2,0,36,0,3]
# list1 = [0,0,1]
# print(list1)
# c1 = Solution()
# c1.moveZeroes(list1)
# print (list1)
