class Solution:
    """
    You are given a large integer represented as an integer array digits, where each digits[i]
    is the ith digit of the integer.
    The digits are ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.
    """

    def plusOne(digits):

        nine_positions = []

        # identify the positions of element(s) in digits that equal 9
        for position, digit in enumerate(digits):
            if digit == 9:
                nine_positions.append(position)

        # if every number in digits is a 9
        if len(nine_positions) == len(digits):
            for position, digit in enumerate(digits):
                digits[position] = 0
            digits.append(1)
            digits.reverse()
            return digits

        # if the trailing digit is not equal to 9
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        # trailing digit(s) equal 9 without all digits equaling 9
        iterate_backwards = len(digits)
        i = 0
        flag_continue = True
        while flag_continue:
            if iterate_backwards - 1 in nine_positions:
                i += 1
                iterate_backwards -= 1
            else:
                flag_continue = False
        # i is equal to the amount of trailing 9's that we need to flip
        for flip_count in range(0, i):
            digits[-1 - flip_count] = 0

        digits[-1 - flip_count - 1] += 1

        return digits







