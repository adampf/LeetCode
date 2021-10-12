# https://youtu.be/8hly31xKli0?t=5304

# recursive depth - number of times the function calls itself
# recursion incurs more space complexity because you create an
#       additional 'thread' (look in debugger window) with every loop

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:  # list[midpoint] > target
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found: ", result)


numbers = range(1000)

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)
