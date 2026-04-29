class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        maxHeight = 0
        res = 0
        for i in range(len(height)):
            maxLeft[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        maxHeight = 0
        for i in range(len(height) - 1, 0, -1):
            maxRight[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        for i in range(len(height)):
            current = min(maxLeft[i], maxRight[i]) - height[i]
            res += current if current > 0 else 0
        return res

        