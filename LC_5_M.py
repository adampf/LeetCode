class Solution:
    """
    Given a string s, return the longest palindromic substring in s.

    Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

    Notes:
        https://www.youtube.com/watch?v=y2BD4MJqV20
        Brute Force Time complexity O(n^3)

    """

    #TODO: This code works properly, but on LC it says I hit a timeout, so need to rewrite this to reduce complexity

    def longestPalindrome(original_string) -> str:

        current_answer = ""
        separator = ""
        iteration = 0

        while iteration != len(original_string):
            test_palindrome = []
            str = original_string[iteration:]

            for x in str:
                test_palindrome.append(x)
                test_string = separator.join(test_palindrome)

                # The remaining code in this 'for' loop checks to see if the test_string is a palindrome
                is_palindrome_flag = True

                # check if length of str is even
                if len(test_string) % 2 == 0:
                    i = 1
                    for pos, x in enumerate(test_string):
                        if test_string[pos] != test_string[-i]:
                            is_palindrome_flag = False
                            break
                        i += 1
                    if is_palindrome_flag == True:
                        if len(current_answer) < len(test_string):
                            current_answer = test_string

                # length of str is odd --- "aabbcbbaa"
                else:
                    if len(test_string) == 1:
                        if len(current_answer) < len(test_string):
                            current_answer = test_string
                        continue

                    split_str = len(test_string) // 2
                    first_str = test_string[0:split_str]
                    second_str = test_string[split_str + 1:]

                    if first_str != second_str[::-1]:
                        is_palindrome_flag = False
                        continue
                    else:
                        if len(current_answer) < len(test_string):
                            current_answer = test_string
            # if true, this means that nothing else could replace current_answer
            if len(current_answer) >= len(str) - 1:
                break
            iteration += 1

        print(current_answer)


    longestPalindrome("abcdefglgfedcba")
    longestPalindrome("abcdefggfedcba")


    longestPalindrome("ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqb"
                      "xbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkd"
                      "rleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoa"
                      "moyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsx"
                      "cvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdf"
                      "opmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlv"
                      "giwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwom"
                      "lyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtec"
                      "qyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjq"
                      "qrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw")
    longestPalindrome("eabcb")
    longestPalindrome("babad")
    longestPalindrome("cbbd")
    longestPalindrome("a")
    longestPalindrome("ac")
    longestPalindrome("ac1")
    longestPalindrome("a1c")
    longestPalindrome("a2332a")



