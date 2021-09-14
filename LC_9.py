import logging

import Logging

Logging.logging_function()
logger = logging.getLogger(__name__)

class LC_9():

    def isPalindrome(x):

        # if there is a negative, then automatically false since there won't be a "-" at the end of the integer
        if x < 0:
            return False

        if x == 0:
            return True

        new_x = x
        digits = []
        digits_reversed = []

        logger.info("Create list of digits")
        while new_x >= 1:
            trailing_digit = new_x % 10
            digits.append(trailing_digit)
            new_x = int((new_x - trailing_digit) / 10)

        # Use a Slice ----- [start:stop:step]
        # start is the index where you start. If it's omitted, Python assumes you want to start at the beginning.
        # stop is where you want to stop. If you omit it, Python assumes you want to go until the end.
        # step is what the -1 is taking advantage of. 1 is the default value. 2 iterates over every other element. -1 iterates over all of the elements, but backwards.

        digits_reversed = digits[::-1]

        logger.info("Comparing both lists (order matters)")
        same = True
        for e, e2 in zip(digits, digits_reversed):
            if e != e2:
                same = False
                print(same)
                return False
        print(same)

        # This code also runs correctly
        # s = 0
        # for x in digits:
        #     if digits[s] != digits_reversed[s]:
        #         same = False
        #         print(same)
        #         return False
        #     s = s + 1

        return same

    # isPalindrome(121)
    # isPalindrome(0)
    isPalindrome(1000021)
