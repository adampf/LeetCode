'''

https://leetcode.com/problems/container-with-most-water/

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
    are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together
    with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

*****************IMAGE OF A BAR GRAPH SHOW ON LEETCODE*****************

Input: height = [1,8,6,2,5,4,8,3,7] --------- List of INT
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
                the max area of water (blue section) the container can contain is 49.

'''

class Solution:

    water_container = [1,8,6,2,5,4,8,3,7]

    def maxArea(self):
        # the container is made up of 4 lines to form a rectangle
        # 2 lines (bottom and top) are equal to the number of lines used to form the width of the container
        # 2 lines (left and right) are equal to the tallest height the box needs to be
        # the example problem forms a 7x7x7x7 container

