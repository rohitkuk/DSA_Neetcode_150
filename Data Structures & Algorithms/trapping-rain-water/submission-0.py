class Solution:
    def trap(self, height: List[int]) -> int:

        lmax = 0
        left_maxes = [0] * len(height)
        for i in range(len(height)):
            left_maxes[i] = lmax
            lmax = max(height[i], lmax)

        rmax = 0
        right_maxes = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            right_maxes[i] = rmax
            rmax = max(height[i], rmax)
        water = 0 
        for i in range(len(height)):
            water+= max(0, min(left_maxes[i], right_maxes[i]) - height[i])
        return water

