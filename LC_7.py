class LC_7():

    # If number starts with a trailing 0, then cut it off
    # If the number has a trailing 0, but then also has a value in the final value, then add it to the end of the final value
    def reverse_signed_integer(x):

        i = 0
        prepped = 0
        original_value = x
        abs_x = abs(x)
        negative_flag = False

        if original_value < 0:
            negative_flag = True

        if x == 0 or x > 2147483648 or x < -2147483648:
            return 0

        while abs_x != 1:

            # checks if there is a trailing 0 and no existing prepped value
            if abs_x % 10 == 0 and prepped == 0:
                abs_x = int(abs_x / 10)
            #
            else:
                # Identify the last digit of abs_x
                trailing_digit = abs_x % 10

                if abs_x == 0 or abs_x > 2147483648 or abs_x < -2147483648:
                    return 0

                # checks if there is only one more digit left to evaluate
                if abs_x == trailing_digit:
                    if x > 0:
                        if negative_flag == True:
                            prepped = ((prepped * 10) + trailing_digit) * -1
                            if prepped == 0 or prepped > 2147483648 or prepped < -2147483648:
                                return 0
                        # if prepped == 0 or prepped > 2147483648 or prepped < -2147483648:
                        #     return 0
                        prepped = ((prepped) * 10) + trailing_digit
                        if prepped == 0 or prepped > 2147483648 or prepped < -2147483648:
                            return 0
                        return prepped
                    if original_value < 0:
                        return ((prepped * 10) + trailing_digit) * -1
                    if prepped == 0 or prepped > 2147483648 or prepped < -2147483648:
                        return 0
                    return trailing_digit

                # Subtract it off of x
                if trailing_digit == 0:
                    temp_integer = abs_x
                else:
                    temp_integer = abs_x - trailing_digit

                abs_x = int(temp_integer / 10)

                # Add it to the beginning of the new number
                # prepper = 10 ** i
                # prepped = (prepped * prepper) + trailing_digit

                prepped = (prepped * 10) + trailing_digit

                i = i + 1

        if original_value < 0:
            final_digit = ((prepped * 10) + 1) * -1
            if x == 0 or x > 2147483648 or x < -2147483648 or final_digit > 2147483648 or final_digit < -2147483648:
                return 0

        else:
            final_digit = (prepped * 10) + 1
            if x == 0 or x > 2147483648 or x < -2147483648 or final_digit > 2147483648 or final_digit < -2147483648:
                return 0

        if x == 0 or x > 2147483648 or x < -2147483648 or final_digit > 2147483648 or final_digit < -2147483648:
            return 0

        return final_digit

    print(reverse_signed_integer(123))
    print(reverse_signed_integer(-123))
    print(reverse_signed_integer(120))
    print(reverse_signed_integer(0))
    print(reverse_signed_integer(900000))

    # This doesn't work .... need to change logic when there are leading 0's
    print(reverse_signed_integer(901000))
    print(reverse_signed_integer(1534236469))
    print(reverse_signed_integer(-901000))
    print(reverse_signed_integer(2147483647))
    print(reverse_signed_integer(-2147483648))









