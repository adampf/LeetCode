import logging

import coloredlogs


coloredlogs.install(level='DEBUG')
logger = logging.getLogger('some.module.name')

class Solution:

    # TODO:
    #  Question 1 would be does this mean the answer has unique characters in the string?
    #  Question 2 would be if I find a substring starting at character number 1, then do I now check
    #       starting at character #2 ?

    def lengthOfLongestSubstring(str):

        if len(str) == 0:
            return 0

        if str.isspace():
            return 1

        check_substring = []
        str_position = 0

        new_string = str
        last_character = str[-1]
        possible_answer = ""

        while new_string:
            for pos, x in enumerate(new_string):
                if x not in check_substring:
                    check_substring.append(x)
                    check_substring_len = len(check_substring)
                else:
                    if len(possible_answer) < len(check_substring):
                        possible_answer = check_substring
                        logger.warning("New possible answer of {} has been added".format(possible_answer))
                    # possible_answer = check_substring
                    check_substring = []

                    str_position += 1
                    new_string = str[str_position:]
                    break
                if len(new_string) == 1:
                    new_string = ""
                    if possible_answer == "":
                        possible_answer = check_substring
                    break

        answer = possible_answer

        return len(answer)

    logger.debug("Now analyzing the string: {}".format("aabaab!bb"))
    logger.info("The answer for the string {} is: {}".format("aabaab!bb", lengthOfLongestSubstring("aabaab!bb")))

    logger.info("The answer for the string {} is: {}".format("c", lengthOfLongestSubstring("c")))

    logger.info("The answer for the string {} is: {}".format(" ", lengthOfLongestSubstring(" ")))


    logger.debug("Now analyzing the string: {}".format("abcadefgh"))
    logger.info("The answer for the string {} is: {}".format("abcadefgh", lengthOfLongestSubstring("abcadefgh")))
    logger.debug("Now analyzing the string: {}".format("abcabcbb"))
    logger.info("The answer for the string {} is: {}".format("abcabcbb", lengthOfLongestSubstring("abcabcbb")))
    logger.debug("Now analyzing the string: {}".format("bbbbb"))
    logger.info("The answer for the string {} is: {}".format("bbbbb", lengthOfLongestSubstring("bbbbb")))
    logger.debug("Now analyzing the string: {}".format("pwwkew"))
    logger.info("The answer for the string {} is: {}".format("pwwkew", lengthOfLongestSubstring("pwwkew")))
    logger.debug("Now analyzing the string: {}".format(""))
    logger.info("The answer for the string {} is: {}".format("", lengthOfLongestSubstring("")))
