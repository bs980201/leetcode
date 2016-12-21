"""325_Maximum_Size_Subarray_Sum_Equals_k."""


class Solution(object):
    """Solution Class."""

    def maxSubArrayLen(self, nums, k):
        """
        max_sub_array_len method.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        map_sum = {}
        map_sum[0] = -1
        max_l, sum_n = 0, 0
        for i, num in enumerate(nums):
            sum_n += num
            if sum_n - k in map_sum:
                max_l = max(i - map_sum[sum_n - k], max_l)
            if sum_n not in map_sum:
                map_sum[sum_n] = i
        return max_l

s = Solution()
list1 = [1, -1, 5, -2, 3]
print ("the answer is = ", s.maxSubArrayLen(list1, 3))
