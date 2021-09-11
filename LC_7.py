class LC_7():

    def reverse_signed_integer(x):

        i = 0
        prepped = 0
        original_value = x

        if x == 0: # or x > 2147483648 or x < -2147483648 or prepped > 2147483648 or prepped < -2147483648:
            return 0

        while x != 1:

            if abs(x) % 10 == 0 and prepped == 0: #AND prepped > 0
                x = int(abs(x) / 10)
            else:
                # Identify the last digit of x
                trailing_digit = abs(x) % 10

                # Subtract it off of x
                if abs(x) == trailing_digit:
                    if x > 0:
                        return (prepped * 10) + trailing_digit
                    if original_value < 0:
                        return trailing_digit * -1
                    return trailing_digit

                if trailing_digit == 0:
                    temp_integer = abs(x)
                else:
                    temp_integer = abs(x) - trailing_digit

                x = int(temp_integer / 10)

                # Add it to the beginning of the new number
                # prepper = 10 ** i
                # prepped = (prepped * prepper) + trailing_digit

                prepped = (prepped * 10) + trailing_digit

                i = i + 1

        if original_value < 0:
            final_digit = ((prepped * 10) + 1) * -1

        else:
            final_digit = (prepped * 10) + 1

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

    # negative_flag = False
    #
    # if x < 0:
    #     negative_flag = True



