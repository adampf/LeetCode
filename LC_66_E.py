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
            print(digits)
            return digits

        # if no number in digits is a 9
        if len(nine_positions) == 0:    # used if input did not have a digit equal to 9
            digits[-1] += 1
            return digits

        # cases that remain:
        # trailing digit(s) equal 9 without all digits equaling 9


        else:   # used if input did at least one digit equal to 9

            if len(nine_positions) == len(digits) - 1 and 0 not in nine_positions:
                for position, digit in enumerate(digits):
                    if position != 0:
                        digits[position] = 0
                digits[0] += 1

                print(digits)
                return digits

            i = 1
            while len(nine_positions) != 0:
                check = 0
                if nine_positions[-1] == len(digits) - i:
                    digits[nine_positions[-1]] = 0
                    check = nine_positions[-1]
                    nine_positions.pop(-1)
                    if len(nine_positions) == 0:
                        digits.append(1)
                        digits.reverse()
                        print(digits)
                        return digits
                    if nine_positions[-1] != (check - 1):
                        digits[-2] += 1
                        return digits
                    else:
                        i += 1
                        continue
                else:
                    # if len(nine_positions) == 0:
                    digits[-1] += 1
                    return digits
                    # else:
                    #     digits[-1] += 1
                    #     return digits

                    i += 1

    # print(plusOne(digits=[1, 2, 3]))
    # print(plusOne(digits=[4, 3, 2, 1]))
    # print(plusOne(digits=[0]))
    # print(plusOne(digits=[9]))
    # print(plusOne(digits=[9,9]))
    # print(plusOne(digits=[9,9,9,9]))
    # print(plusOne(digits=[9,2,3,9]))
    # print(plusOne(digits=[9,4,5,0]))
    # print(plusOne(digits=[9,4,5,0, 9]))
    # print(plusOne(digits=[9,4,5,0, 4]))
    # print(plusOne(digits=[9,4,5,0, 0, 4]))
    # print(plusOne(digits=[9,4,5,0, 9, 0, 4]))
    # print(plusOne(digits=[8, 9, 9, 9]))
    # print(plusOne(digits=[9,8,7,6,5,4,3,2,1,0]))
    print(plusOne(digits=[9,8,9,9]))


    """
    if the last digit is not equal to 9, then assemble the number and add 1 to it
    """







