import logging
import math

import Logging
import coloredlogs

Logging.logging_function()
logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')
logger = logging.getLogger('some.module.name')
logger.info("this is an informational message")

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

class LC_37():

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    # def sudoku_solver(board):

        # TODO: Keys to solving a sudoku
        # 1) all rows / columns must add up to 45
        # 2) all rows / columns can only have each digit once
        # 3) search for any rows / columns with one missing space

        # TODO: Maybe start by calculating all possible values per row / column

    # Finds values that do not live in each row / column
    def find_missing_digits(lists):

        missing_values = [[] for i in range(9)]

        # i stands for the 1-9 numbers that must fill rows / columns in Sudoku
        i = 1
        # j stands for the row numbers that we are testing
        j = 0
        # k stands for the position number within the row of the new list
        k = 0

        logger.info("*********Begin calculating missing numbers in each row*********")
        for x in range(len(lists)):
            for y in range(len(lists)):

                # if the text version of the number i is not found in the j'th row
                if str(i) not in lists[j]:
                    missing_values[k].append(i)
                    # print(test)
                i += 1
            logger.debug("Row {} is missing the numbers: ".format(j+1))
            logger.info(missing_values[k])
            k += 1
            j += 1
            i = 1

        logger.critical("Each row's missing numbers: ")
        logger.info(missing_values)
        logger.warning("*********End calculating missing numbers in each row*********")

        return missing_values

    # Same format as 'board', but by column instead of by row
    def transpose_rows_to_columns(lists):

        transposed = [[] for i in range(9)]

        logger.info("*********Begin creating List for column values *********")
        for x in range(len(lists)):
            for y in range(len(lists)):
                transposed[x].append(lists[y][x])
        print(transposed)
        logger.warning("*********End creating List for column values *********")

        return transposed

    # TODO: Calculate the number that the missing digits of each row must add up to equal
    # def sum_row_value(self):
        # In the case of a 9x9, that number is 45

    # TODO: Calculate the number that the missing digits of each column must add up to equal
    # def sum_column_value(self):
        # In the case of a 9x9, that number is 45

    # TODO: Create list for each 3x3 grid
    # 9 lists
    # List #1 is the intersection of the first 3 rows AND the first 3 columns: 1,1 1,2 1,3 2,1 2,2 2,3 3,1 3,2 3,3
    # List #2 is the intersection of rows 1,2,3 and columns 4,5,6
    # List #3 is the intersection of rows 1,2,3 and columns 7,8,9
    def create_lists_for_grids(row_list, column_list):

        # if gridnum is 1 then rows 1,2,3 and columns 1,2,3
        # if gridnum is 2 then rows 1,2,3 and columns 4,5,6
        # if gridnum is 3 then rows 1,2,3 and columns 7,8,9

        grid_elements = [[] for i in range(9)]

        for gridnum in range(1, 10):
            # grid num 1, 4, 7
            if gridnum % 3 == 1:
                starting_column_position = 1
                ending_column_position = 3
                if gridnum == 1:
                    starting_row_position = 1
                    ending_row_position = 3
                if gridnum == 4:
                    starting_row_position = 4
                    ending_row_position = 6
                if gridnum == 7:
                    starting_row_position = 7
                    ending_row_position = 9
            # grid num 2, 5, 8
            elif gridnum % 3 == 2:
                starting_column_position = 4
                ending_column_position = 6
                if gridnum == 2:
                    starting_row_position = 1
                    ending_row_position = 3
                if gridnum == 5:
                    starting_row_position = 4
                    ending_row_position = 6
                if gridnum == 8:
                    starting_row_position = 7
                    ending_row_position = 9
            # grid num 3, 6, 9
            elif gridnum % 3 == 0:
                starting_column_position = 7
                ending_column_position = 9
                if gridnum == 3:
                    starting_row_position = 1
                    ending_row_position = 3
                if gridnum == 6:
                    starting_row_position = 4
                    ending_row_position = 6
                if gridnum == 9:
                    starting_row_position = 7
                    ending_row_position = 9

            logger.debug("starting_row_position is: {}".format(starting_row_position))
            logger.debug("ending_row_position is: {}".format(ending_row_position))
            logger.debug("starting_column_position is: {}".format(starting_column_position))
            logger.debug("ending_column_position is: {}".format(ending_column_position))

            # this means that we want to return a new list containing all 9 elements in grid number X
            # in the case of gridnum = 2, then we want rows 1-3 and columns 4-6
            i = starting_row_position
            j = starting_column_position

            for x in range(3):
                for y in range(3):
                    grid_elements[gridnum-1].append(row_list[i-1][j-1])
                    j += 1
                i += 1
                j = starting_column_position

            logger.debug(grid_elements)

        return grid_elements

    def test_digits(board, missing_digits_rows, missing_digits_columns, missing_digits_grid):

        # find the first blank space
        # check if digit 1 exists in the row
        # check if digit 1 exists in the column
        # check if digit 1 lives in the grid
        # if true to ANY of these, then digit 1 cannot live in that spot

        potential_solutions = [[] for cell in range(81)]
        cell_value = 0

        logger.critical("Each row is missing the following values: {}".format(missing_digits_rows))
        logger.critical("Each column is missing the following values: {}".format(missing_digits_columns))
        logger.critical("Each grid is missing the following values: {}".format(missing_digits_grid))

        # used to identify the row of the board
        i = 0
        # used to identify the column of the board
        j = 0
        # used to iterate through digits 1 through 9 like in a Sudoku game
        k = 1
        # used to identify the element in missing_digits_rows
        m = 0
        # used to identify the element of element m in missing_digits_rows
        p = 0

        for x in range(9):
            for y in range(9):
                for z in range(9):

                    logger.debug("Now testing the digit {} at row {} column {}".format(k, i+1, j+1))

                    # need to be able to identify what grid we are in at any point
                    if i + 1 >= 1 and i + 1 <= 3:
                        # this means we are in gridnum 1, 2, or 3
                        if j + 1 >= 1 and j + 1 <= 3:
                            gridnum = 1
                        if j + 1 >= 4 and j + 1 <= 6:
                            gridnum = 2
                        if j + 1 >= 7 and j + 1 <= 9:
                            gridnum = 3
                    elif i + 1 >= 4 and i + 1 <= 6:
                        # this means we are in gridnum 4, 5, or 6
                        if j + 1 >= 1 and j + 1 <= 3:
                            gridnum = 4
                        if j + 1 >= 4 and j + 1 <= 6:
                            gridnum = 5
                        if j + 1 >= 7 and j + 1 <= 9:
                            gridnum = 6
                    elif i + 1 >= 7 and i + 1 <= 9:
                        # this means we are in gridnum 7, 8, or 9
                        if j + 1 >= 1 and j + 1 <= 3:
                            gridnum = 7
                        if j + 1 >= 4 and j + 1 <= 6:
                            gridnum = 8
                        if j + 1 >= 7 and j + 1 <= 9:
                            gridnum = 9
                    else:
                        logger.critical("Something went wrong because gridnum is not equal to 1 through 9")
                    logger.debug("gridnum is equal to {}".format(gridnum))

                    # if a spot on the board is blank
                    if board[i][j] == ".":
                        logger.debug("Missing value at row {} column {}".format(i+1, j+1))
                        # logger.critical(missing_digits_rows[m][p])

                        # check if the first digit from our known missing values (rows) exists in our current row
                        if k in missing_digits_rows[i]:
                            # this means digit "k" lives in the row
                            missing_from_row = True

                        # check if the first digit from our known missing values (columns) exists in our current row
                        if k in missing_digits_columns[j]:
                            # this means digit "k" lives in the column
                            missing_from_column = True

                        # debugggg = LC_37.create_lists_for_grids(missing_digits_rows, missing_digits_columns, k)
                        # logger.critical(debugggg)
                        # check if the first digit from our known missing values (grid) exists in our current row
                        if k in missing_digits_grid[gridnum-1]:
                            # this means digit "k" lives in the grid
                            missing_from_grid = True

                        if missing_from_row and missing_from_column and missing_from_grid:
                            logger.warning("Digit {} could potentially live in row {} column {}".format(k, i + 1, j + 1))
                            potential_solutions[cell_value].append(k)
                            logger.warning("Potential solutions are now: {}".format(potential_solutions))
                        else:
                            logger.warning("Digit {} CANNOT live in row {} column {}".format(k, i + 1, j + 1))
                    cell_value += 1
                    missing_from_row = False
                    missing_from_column = False
                    missing_from_grid = False

                    j += 1
                i += 1
                j = 0
            k += 1
            i = 0
            cell_value = 0
        logger.info("Potential solutions are: {}".format(potential_solutions))
        logger.info(potential_solutions[38])

        # potential_solutions[21] = "6"

        for w in potential_solutions:
            if len(w) == 1:
                logger.info("We can fill in the empty cell {} with the value {}".format(potential_solutions.index(w)+1, w))
                # TODO: Append value to board
                board_row = (potential_solutions.index(w) + 1) / 9
                board_row = math.ceil((potential_solutions.index(w)+1) / 9)
                board_column = (potential_solutions.index(w)+1) % 9

                logger.warning("Replacing the empty value with {}".format(w[0]))
                board[board_row - 1][board_column - 1] = w[0]

                # TODO: Test cases when w is positioned in 1st row, 1st column, 9th row, 9th column


    logger.warning("Find the missing digits in each row of the Sudoku board")
    missing_digits_rows = find_missing_digits(board)
    logger.warning(
        "Transpose rows into columns so that we can find the missing digits in each column of the Sudoku board")
    change_rows_to_columns = transpose_rows_to_columns(board)
    logger.warning("Find the missing digits in each column of the Sudoku board")
    missing_digits_columns = find_missing_digits(change_rows_to_columns)
    change_grid_to_rows = create_lists_for_grids(board, change_rows_to_columns)
    missing_digits_grid = find_missing_digits(change_grid_to_rows)
    test_digits(board, missing_digits_rows, missing_digits_columns, missing_digits_grid)
    logger.debug(board)







