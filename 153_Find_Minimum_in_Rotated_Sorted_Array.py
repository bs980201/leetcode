class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # mid = int(len(nums)/2)+1

        # nums1 = nums[0:mid]
        # nums2 = nums[mid:len(nums)]

        n = len(nums)
        if n == 1:
            return nums[0]
        head = 0
        tail = n-1

        while head != tail:
            mid = (head+tail)/2 + 1
            # mid = head+(tail-head)/2
            if nums[head] < nums[tail]:
                return nums[head]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[head] < nums[mid]:
                head = mid
            else:
                tail = mid - 1
        return [head]

list1 = [2,3,4,1,5]
print(list1)
s = Solution()
print (s.findMin(list1))
