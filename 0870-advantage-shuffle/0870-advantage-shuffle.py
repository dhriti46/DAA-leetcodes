class Solution(object):
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        sorted_nums2 = sorted(
            [(value, i) for i, value in enumerate(nums2)]
        )

        result = [0] * len(nums2)
        left = 0
        right = len(nums2) - 1

        for num in nums1:
            if num > sorted_nums2[left][0]:
                result[sorted_nums2[left][1]] = num
                left += 1
            else:
                result[sorted_nums2[right][1]] = num
                right -= 1

        return result