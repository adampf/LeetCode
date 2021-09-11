#14 - Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

'''
Approach:

1) grab first letter of word one and compare to all other words in the array of strings



'''

class Solution:

    def longestCommonPrefix(strs):
        print(strs)
        print(strs[2])

        first_word = strs[0]
        second_word = strs[1]
        third_word = strs[2]
        fourth_word = strs[3]
        print(second_word[4])
        print("#######################################################")

        characters = 0

        # grab first character of first word
        for x in first_word:
            first_character = first_word[0]
            print(first_character)

        print("#######################################################")

        placeholder = []
        # print first character of all words in the array of strings
        for x in strs:
            print(x[0])
            # add each first letter to an empty array
            placeholder.append(x[0])
        print(placeholder)

        print("#######################################################")

        # identify which (if any) elements are equal to each other
        for p in placeholder:
            print(p)
            print(placeholder.index())
            # if placeholder.index(p) == placeholder.index(p):
            #     print("99")
            # else:
            #     print("No matching first characters")

        result = placeholder.cou

            # print(secondWord[characters])
            # characters = characters+1

    longestCommonPrefix(["first", "second", "third", "thilakwefl"])
