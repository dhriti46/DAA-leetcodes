
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maximum = 0

        while left < right:
            width = right - left
            h = min(height[left], height[right])

            area = width * h
            maximum = max(maximum, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum        