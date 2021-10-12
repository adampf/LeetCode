class Solution:
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Constraints:
    1 <= n <= 45
    """

    # TODO: Question you should have clarified - Do you have to hit n exactly, or for example if
    #  n = 3 can you do 2 one steps and 1 two steps?

    def climbStairs(n):

        # # if n is 1 or 2
        # if n in range(1, 3):
        #     # if n is odd
        #     if n % 2 != 0:
        #         return n + (n // 2)
        #
        #     # if n is even
        #     else:
        #         return n + (n // 2) - 1
        # else:   # means n >= 3
        #     # if n is odd
        #     if n % 2 != 0:
        #         return n - (n // 2)
        #
        #     # if n is even
        #     else:
        #         return n - (n // 2) + 1

        max_two_steps = n // 2
        print("The maximum number of 2-steps that can be taken is: {}".format(max_two_steps))

    print(climbStairs(1))
    print(climbStairs(2))
    print(climbStairs(3))
    print(climbStairs(4))
    print(climbStairs(5))


