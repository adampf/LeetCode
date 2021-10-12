import logging
import math

import Logging
import coloredlogs

# Logging.logging_function()
# logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')
logger = logging.getLogger('some.module.name')

# lists vs. tuples - https://jtauber.com/blog/2006/04/15/python_tuples_are_not_just_constant_lists/

'''
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

Do not return anything, modify board in-place instead.
'''

# First test case
# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# Second test case
board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]


class LC_37_refactor():

    # This counts the number of cells that are blank on the board
    def count_board_blanks(board):

        count = 0

        for x in board:
            for y in x:
                if y == ".":
                    count += 1

        return count

    # Finds values that do not currently live in the board's rows and columns
    def find_missing_digits(lists):

        missing_values = [[] for i in range(9)]

        i = 1         # i stands for the 1-9 numbers that must fill rows / columns in Sudoku
        j = 0         # j stands for the row numbers that we are testing
        k = 0         # k stands for the position number within the row of the new list

        # logger.debug("*********Begin calculating missing numbers in each row*********")
        for x in range(len(lists)):
            for y in range(len(lists)):

                # if the text version of the number i is not found in the j'th row
                if str(i) not in lists[j]:
                    missing_values[k].append(i)
                i += 1
            # logger.debug("Row {} is missing the numbers: {}".format(j+1, missing_values[k]))
            k += 1
            j += 1
            i = 1

        # logger.debug("The missing numbers are: {}".format(missing_values))
        # logger.info("*********End calculating missing numbers in each row*********")

        logger.debug("\n" + "find_missing_digits() evaluates to:" + "\n" + "\n".join(str(h) for h in missing_values))

        return missing_values

    # Same format as 'board', but each list is the board's columns instead of the board's rows
    def transpose_rows_to_columns(lists):

        transposed = [[] for i in range(9)]

        # logger.info("*********Begin creating List for column values *********")
        for x in range(len(lists)):
            for y in range(len(lists)):
                transposed[x].append(lists[y][x])
        # logger.info("*********End creating List for column values *********")

        return transposed

    # Same format as 'board', but each list is the board's grids instead of the board's rows
    def transform_rows_to_grids(rows):

        grids = [[] for i in range(9)]

        k = 0   # used for the row number of grids

        # logger.warning("\n" + "transpose_rows_to_grids() is using the board:" + "\n" + "\n".join(str(h) for h in rows))

        temp_1 = 0
        temp_2 = 0
        i = 0 + temp_2
        j = 0 + temp_1
        for final in range(3):
            for x in range(3):
                j = 0 + temp_1
                i = 0 + temp_2
                for y in range(3):
                    for z in range(3):
                        grids[k].append(rows[i][j])
                        j += 1
                    i += 1
                    j = 0 + temp_1
                    # logger.info("Board so far is: {}".format(grids))
                k += 1
                temp_1 += 3
                i = 0 + temp_2
                # logger.critical("\n" + "transpose_rows_to_grids() evaluates to:" + "\n" + "\n".join(str(h) for h in grids))
            temp_2 += 3
            temp_1 = 0

        return grids

    # Determines which values could potentially live in each cell of the board
    def possible_values(board, columns_as_rows, grids_as_rows, missing_from_rows, missing_from_columns, missing_from_grids):

        i = 0   # denotes the row of board
        j = 0   # denotes the column of board
        k = 0   # denotes the element in the 'missing' list that we are checking

        possible_solutions = [[[] for i in range(9)] for j in range(9)]

        while i < 9:
            # j = 0 ###########!!!!!!!!!!!!!!!!!!!!!!!!!#################################******************#######################
            if len(missing_from_rows[i]) == 0:
                i += 1
            else:
                logger.critical("ROW'S missing digits we are checking:    {}".format(missing_from_rows[i]))  ####################################################################################
                for y in range(len(missing_from_rows[i])):

                    if len(missing_from_rows[i]) == 0:
                        break

                    grid_num = 3 * (i // 3) + (j // 3) + 1

                    # checks to see if the cell is empty (not solved for)
                    if board[i][j] == ".":
                        # run main logic
                        # what is the first value that we will evaluate for board[i][j] ?
                        testing_digit = missing_from_rows[i][k]

                        # logger.debug("ROW'S missing digits we are checking:    {}".format(missing_from_rows[i]))####################################################################################
                        # logger.warning("Evaluating {} at board[{}][{}]".format(testing_digit, i, j))####################################################################################
                        # logger.debug("COLUMN'S missing digits we are evaluating: {}".format(missing_from_columns[j]))####################################################################################
                        # logger.debug("GRID'S missing digits we are evaluating:   {}".format(missing_from_grids[grid_num - 1]))####################################################################################

                        # checks to see if the digit we are testing is missing in column[j]
                        # if testing_digit in (missing_from_columns[j] and missing_from_grids[grid_num - 1]):
                        if testing_digit in missing_from_columns[j] and testing_digit in missing_from_grids[grid_num - 1]:

                            # this means testing_digit could possibly live in the current cell
                            possible_solutions[i][j].append(testing_digit)
                            logger.info("Appending {} to possible_solutions[{}][{}]".format(testing_digit, i, j))####################################################################################
                        else:
                            logger.info("Digit {} already lives in either the column or the grid".format(testing_digit))####################################################################################
                            if j == 8 and k >= len(missing_from_rows[i])-1:
                                j = 0
                                i += 1
                                k = 0
                                break

                        # Checks to make sure we are not trying to test more numbers than are missing from the row
                        if k < len(missing_from_rows[i])-1:
                            # logger.debug("Check the next number at board[{}][{}]".format(i, j)) ###########################################
                            k += 1
                        # But if we are, then reset k, and move over one column
                        else:

                            if j == 8:
                                k = 0
                                j = 0
                                i += 1
                                logger.critical("Moving on to the next cell at board[{}][{}]".format(i, j))

                            else:
                                k = 0
                                j += 1
                                logger.critical("Moving on to the next cell at board[{}][{}]".format(i, j))

                    # means this cell has already been solved for
                    else:
                        logger.debug("board[{}][{}] has already been solved for".format(i, j))####################################################################################
                        # skip that cell in the board and move to the next
                        if j == 8:
                            j = 0
                            i += 1
                        else:
                            j += 1
                            break
                            # logger.critical("ROW'S missing digits we are checking:    {}".format(missing_from_rows[i]))  ####################################################################################

        return possible_solutions

    # searches for cells that can only have one possible value: len == 1
    def find_single_solutions(possible_solutions):

        row = 1
        column = 1

        append1 = []
        append2 = []

        while row <= 9:
            for x in possible_solutions:
                for y in x:
                    if len(y) == 1:
                        append2.append(y[0])
                        append2.append(row)
                        append2.append(column)
                        append1.append(append2)
                        append2 = []
                    column += 1
                row += 1
                column = 1

        return append1

    # takes list of lists from find_single_solutions() and enters them into the board
    def modify_board(board, append_values):

        for x in append_values:
            board[x[1]-1][x[2]-1] = str(x[0])

        return board

    # This method identifies numbers per row that can only live in one cell
    def find_single_options(possible_solutions, missing_from_rows, board):

        frequency_count = 0
        row_count = 0
        column_count = 0

        for x in possible_solutions:
            row_missing = missing_from_rows[row_count]
            for z in row_missing:
                for t in x:
                    if z in t:
                        frequency_count += 1
                        column_identifier = column_count
                        if frequency_count > 1:
                            logger.debug("The value {} could live in multiple cells of the row".format(z))
                            logger.debug("Moving onto the next digit missing from the row")
                            frequency_count = 0
                            column_count += 1
                            break
                    column_count += 1
                if frequency_count == 1:
                    logger.debug("Appending the value {} to board[{}][{}]".format(z, row_count, column_identifier))
                    board[row_count][column_identifier] = str(z)
                    column_count = 0
                    column_identifier = 0
                    break

                    # return board
                column_count = 0
                column_identifier = 0
            row_count += 1

        return board

    # TODO: It's currently working for grids. Now need to make it work for columns and rows
    def find_two_pairs_grid(possible_solutions_grids, missing_from_grids):

        # for x, element in enumerate(missing_from_grids):
        #     logger.debug("{}, {}".format(x, element))

        # check rows, columns and grids
        # if row has 4 or more open cells
        # then check for frequency of digits in those cells
        # if 2 or more digits have a frequency == 2
        # then run 4/8 logic

        # happy path is grid #1 so we will hardcode this scenario first
        temp2 = []
        #TODO: Make this dynamic instead of static
        grid_num = 1

        for x in missing_from_grids[0]:
            position = 0
            temp3 = []

            for y in possible_solutions_grids[0]:
                # logger.debug("Looking for digit {} in {}".format(x, y))
                position += 1

                if x in y:
                    # count += 1
                    temp3.append([x, position-1])

                if len(temp3) > 2:
                    break
            if len(temp3) == 2:
                # temp.append(x)
                temp2.append(temp3)

        # Now temp[] contains all of the digits that have a frequency of 2
        # TODO: Double check this logic when debugging
        if len(temp2) != 2:
            # move onto the next row / column / grid
            logger.debug("aslkfjlksdjf")
        else:
            logger.info("value/position {}".format(temp2))

            # remove all possible values except for what is found in temp2
            possible_solutions_grids[0][temp2[0][0][1]] = [temp2[0][0][0], temp2[1][0][0]]
            possible_solutions_grids[0][temp2[0][1][1]] = [temp2[0][0][0], temp2[1][0][0]]
            logger.debug(possible_solutions_grids[0])
            logger.debug("\n" + "GRIDS --- Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(
                str(h) for h in possible_solutions_grids))

        # if this code was being run on a grid, then we have to transform the result back into the row format

        # possible_solutions =

        return possible_solutions_grids

    # def find_two_pairs_row(possible_solutions, missing_from_rows):

    # def find_two_pairs_column(possible_solutions, missing_from_columns):

    def find_digit_three_rows(missing_from_rows, possible_solutions):

        # for x, element in enumerate(missing_from_grids):
        #     logger.debug("{}, {}".format(x, element))

        # check rows, columns and grids
        # if row has 4 or more open cells
        # then check for frequency of digits in those cells
        # if 2 or more digits have a frequency == 2
        # then run 4/8 logic

        # happy path is grid #1 so we will hardcode this scenario first
        subgrid1 = []
        subgrid2 = []
        subgrid3 = []
        # TODO: Make this dynamic instead of static
        grid_num = 1
        row1 = 0
        row2 = 3
        row3 = 7

        logger.info("\n" + "Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(str(h)
                                        for h in missing_from_rows))

        for x in missing_from_rows[row1]:
            position = 0
            temp_subgrid1 = []

            for y in possible_solutions[row1]:
                # logger.debug("Looking for digit {} in {}".format(x, y))
                position += 1

                if x in y:
                    # count += 1
                    temp_subgrid1.append([x, position - 1])

                if len(temp_subgrid1) > 3:
                    break
            if len(temp_subgrid1) == 3:
                # temp.append(x)
                subgrid1.append(temp_subgrid1)

        for x in missing_from_rows[row2]:
            position = 0
            temp_subgrid2 = []

            for y in possible_solutions[row2]:
                # logger.debug("Looking for digit {} in {}".format(x, y))
                position += 1

                if x in y:
                    # count += 1
                    temp_subgrid2.append([x, position - 1])

                if len(temp_subgrid2) > 3:
                    break
            # TODO: hardcoded 2 for the specific use case, would need to change systematically
            if len(temp_subgrid2) == 2:
                # temp.append(x)
                subgrid2.append(temp_subgrid2)

        for x in missing_from_rows[row3]:
            position = 0
            temp_subgrid3 = []

            for y in possible_solutions[row3]:
                # logger.debug("Looking for digit {} in {}".format(x, y))
                position += 1

                if x in y:
                    # count += 1
                    temp_subgrid3.append([x, position - 1])

                if len(temp_subgrid3) > 3:
                    break

            if len(temp_subgrid3) == 3:
                # temp.append(x)
                subgrid3.append(temp_subgrid3)

        logger.debug(subgrid1)
        logger.debug(subgrid2)
        logger.debug(subgrid3)

        temp1 = []
        for x in subgrid1:
            if x[0][0] == 5:
                temp1.append(x[0][1])
                temp1.append(x[1][1])
                temp1.append(x[2][1])

        temp2 = []
        for x in subgrid2:
            if x[0][0] == 5:
                temp2.append(x[0][1])
                temp2.append(x[1][1])
                # TODO: Comment back in for systematic approach
                # temp2.append(x[2][1])

        temp3 = []
        for x in subgrid3:
            if x[0][0] == 5:
                temp3.append(x[0][1])
                temp3.append(x[1][1])
                temp3.append(x[2][1])

        # This means 5 has to live in column 1, 2, 8
        # So any other cells that have 5 as a possibility within column 1, 2, 8 it needs to be removed

        counter_row = 0
        counter_column = 0
        for x in possible_solutions:
            # if
            if 5 in x[0] and counter_row not in (0, 3, 7):
                x[0].remove(5)
            if 5 in x[1] and counter_row not in (0, 3, 7):
                x[1].remove(5)
            if 5 in x[7] and counter_row not in (0, 3, 7):
                x[7].remove(5)

            counter_row += 1

        logger.info("\n" + "Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(str(h)
                                        for h in possible_solutions))

        return possible_solutions

    # TODO: Currently, we have functions to generate rows, columns, and grids, as well as their missing values \
    # TODO: cont.. of each element of those 3. We can also check each cell in the board to see what values
    # TODO: cont.. could possibly live there. Up until now we have not solved for any cells on the board
    # TODO: Now we can go through and append values for the 'possible_solutions' with length 1

    loop_check = 0
    loop_counter = 0

    logger.warning("\n" + "Board to be solved is:" + "\n" + "\n".join(str(h) for h in board))
    num_blanks = count_board_blanks(board)
    logger.debug("The board currently has {} blanks".format(num_blanks))

    while num_blanks > 0:

        logger.warning("Loops so far: {}".format(loop_counter))

        logger.info("Each row is missing the following values:")
        missing_from_rows = find_missing_digits(board)
        logger.warning("Transposing rows into columns")
        columns_as_rows = transpose_rows_to_columns(board)
        logger.debug("\n" + "transpose_rows_to_columns() evaluates to:" + "\n" + "\n".join(str(h) for h in columns_as_rows))
        logger.info("Each column is missing the following values:")
        missing_from_columns = find_missing_digits(columns_as_rows)
        grids_as_rows = transform_rows_to_grids(board)
        logger.debug("\n" + "transpose_rows_to_grids() evaluates to:" + "\n" + "\n".join(str(h) for h in grids_as_rows))
        logger.info("Each grid is missing the following values:")
        missing_from_grids = find_missing_digits(grids_as_rows)
        possible_solutions = possible_values(board, columns_as_rows, grids_as_rows, missing_from_rows, missing_from_columns, missing_from_grids)
        logger.warning("\n" + "Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(str(h) for h in possible_solutions))
        append_values = find_single_solutions(possible_solutions)
        logger.debug("New values to append to the main board (value, row, column): {}".format(append_values))
        updated_board = modify_board(board, append_values)
        logger.info("\n" + "Board has been updated as follows:" + "\n" + "\n".join(str(h) for h in updated_board))
        num_blanks = count_board_blanks(board)
        logger.debug("The board currently has {} blanks".format(num_blanks))
        single_options = find_single_options(possible_solutions, missing_from_rows, board)
        logger.info("\n" + "Board has been updated as follows:" + "\n" + "\n".join(str(h) for h in board))

        # #TODO: I don't think this new possible solutions board is being utilized because of the possible solutions
        # # TODO: definition above ^^^^^^^^^
        # # ***************************
        possible_solutions_grids = transform_rows_to_grids(possible_solutions)
        # logger.debug("\n" + "GRIDS --- Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(
        #     str(h) for h in possible_solutions_grids))
        #
        # two_pairs_grid = find_two_pairs_grid(possible_solutions_grids, missing_from_grids)
        #
        # logger.info("\n" + "Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(str(h)
        #                         for h in transform_rows_to_grids(two_pairs_grid)))
        # # ***************************

        # possible_solutions = transform_rows_to_grids(two_pairs_grid)


        # If true, then this means the loop did not solve for any additional spaces, and therefore would be an infinite loop we need to break
        if num_blanks == loop_check:
            break
        loop_check = num_blanks
        loop_counter += 1

    logger.info("\n" + "FINAL board with {} missing values after {} loops:".format(num_blanks, loop_counter) + "\n"
                + "\n".join(str(h) for h in board))

    # find_digit_three_rows(missing_from_rows, possible_solutions)
    #
    # def brute_force(board, possible_solutions):
    #
    #     logger.debug("\n" + "current boardddddddd:" + "\n" + "\n".join(str(h) for h in board))
    #     logger.debug("\n" + "original possible_solutions:" + "\n" + "\n".join(str(h) for h in possible_solutions))
    #
    #     # 1) Find a cell with only two possible values
    #     # 2) Hypothetically use the first value
    #     # 3) See what is impacted by this
    #
    #     # rinse and repeat step 2 through x for the second possible value in the original cell
    #
    #     # implement step 1:
    #     hypothetical = []
    #
    #     for x, rows in enumerate(possible_solutions):
    #         if len(hypothetical) == 2:
    #             break
    #         for y, cells in enumerate(rows):
    #             logger.debug("{}, {}".format(y, cells))
    #             if len(cells) == 2:
    #                 logger.debug("row {} column {}".format(x, y))
    #                 hypothetical = [x, y]
    #                 break
    #
    #     test_board_row = hypothetical[0]
    #     test_board_column = hypothetical[1]
    #
    #     first_test_value = cells[0]
    #     second_test_value = cells[1]
    #     logger.debug("The cell we will test is board[{}][{}]".format(test_board_row, test_board_column))
    #     logger.warning("The values we will test are {} and {}".format(first_test_value, second_test_value))
    #
    #     #implement step 2:
    #     board_first_value = possible_solutions
    #
    #     logger.debug("set cell in possible_values to blank")
    #     board_first_value[test_board_row][test_board_column] = []
    #
    #     logger.info("Now testing the first value of {}".format(first_test_value))
    #     temp_remove_digits = []
    #     for t, value in enumerate(possible_solutions[test_board_row]):
    #         if first_test_value in value:
    #             value.remove(first_test_value)
    #             temp_remove_digits.append([first_test_value, t])
    #     logger.warning("Row after removing the first_test_value {}".format(possible_solutions[test_board_row]))
    #     logger.warning(temp_remove_digits)
    #
    #     # LC_37_refactor.find_single_options(possible_solutions, missing_from_rows, board):
    #     #     logger.debug("asdf")
    #
    #
    #
    #
    #     logger.info("Now testing the second value of {}".format(cells[1]))
    #
    #
    #
    #     logger.debug("\n" + "test_first_value" + "\n" + "\n".join(str(h) for h in board_first_value))
    #
    #
    #     return board
    #
    # brute_force(board, possible_solutions)

    def backtracker(board, missing_from_rows, missing_from_columns, missing_from_grids, possible_solutions, possible_solutions_grids):

        logger.debug(board)
        logger.debug("missing_from_rows {}".format(missing_from_rows))
        logger.debug("missing_from_columns {}".format(missing_from_columns))
        logger.debug("missing_from_grids {}".format(missing_from_grids))

        logger.warning("\n" + "Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(
            str(h) for h in possible_solutions))
        logger.warning("\n" + "GRIDS --- Possible solutions - possible_values evaluates to:" + "\n" + "\n".join(
            str(h) for h in possible_solutions_grids))






        hmmmmmm = 0
        new_start_flag = True

        for x, row_value in enumerate(possible_solutions):
            for y, cell_value in enumerate(row_value):

                if len(cell_value) == 0:
                    logger.debug("board[{}][{}] has already been solved".format(x, y))
                    continue
                elif new_start_flag:
                    testing_cell_position = [x, y]
                    logger.warning("Starting brute force at board[{}][{}]".format(x, y))
                    testing_cell_value = cell_value
                    digit = cell_value[y]
                    logger.debug("Testing the digit = {}".format(digit))
                    logger.debug("Setting the hard coded digit of {} to board[{}][{}]".format(digit, x, y))
                    cell_value = digit
                    new_start_flag = False
                    continue
                elif digit in cell_value:
                    logger.debug("Remove digit {} from next cell value {} at board[{}][{}]".format(digit, cell_value, x, y))
                    cell_value.remove(digit)
            logger.info("Finished removing digit {} from row {}".format(digit, x))
            logger.debug("Row from possible_solutions is now equal to: {}".format(row_value))
            logger.debug("Now need to do the same for column and grid")


        logger.critical(possible_solutions)






        return board

    backtracker(board, missing_from_rows, missing_from_columns, missing_from_grids, possible_solutions, possible_solutions_grids)






















