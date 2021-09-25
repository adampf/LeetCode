import logging
import math

import Logging
import coloredlogs

Logging.logging_function()
logger = logging.getLogger(__name__)

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

class LC_37():

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    # Finds values that do not currently live in the board's rows and columns
    def find_missing_digits(lists):

        missing_values = [[] for i in range(9)]

        i = 1         # i stands for the 1-9 numbers that must fill rows / columns in Sudoku
        j = 0         # j stands for the row numbers that we are testing
        k = 0         # k stands for the position number within the row of the new list

        logger.info("*********Begin calculating missing numbers in each row*********")
        for x in range(len(lists)):
            for y in range(len(lists)):

                # if the text version of the number i is not found in the j'th row
                if str(i) not in lists[j]:
                    missing_values[k].append(i)
                i += 1
            logger.debug("Row {} is missing the numbers: {}".format(j+1, missing_values[k]))
            k += 1
            j += 1
            i = 1

        logger.warning("Each row's missing numbers: {}".format(missing_values))
        logger.info("*********End calculating missing numbers in each row*********")

        return missing_values

    # Same format as 'board', but each list is the board's columns instead of the board's rows
    def transpose_rows_to_columns(lists):

        transposed = [[] for i in range(9)]

        logger.info("*********Begin creating List for column values *********")
        for x in range(len(lists)):
            for y in range(len(lists)):
                transposed[x].append(lists[y][x])
        logger.info("*********End creating List for column values *********")

        return transposed

    def create_lists_for_grids(row_list, column_list):

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

            logger.debug("Grid #{} has Rows {} through {} and Columns {} through {}".format(
                        gridnum, starting_row_position, ending_row_position,
                        starting_column_position, ending_column_position))

            i = starting_row_position
            j = starting_column_position

            # create lists containing values of each grid
            for x in range(3):
                for y in range(3):
                    grid_elements[gridnum-1].append(row_list[i-1][j-1])
                    j += 1
                i += 1
                j = starting_column_position

        logger.debug(grid_elements)

        return grid_elements

    def test_digits(board, missing_digits_rows, missing_digits_columns, missing_digits_grid):

        # find each blank space
        # check if digit 1 exists in the row
        # check if digit 1 exists in the column
        # check if digit 1 lives in the grid
        # if true to ANY of these, then digit 1 cannot live in that spot
        # rinse and repeat for digit 2, 3, ... , 9

        potential_solutions = [[] for cell in range(81)]
        cell_value = 0

        logger.critical("Each row is missing the following values: {}".format(missing_digits_rows))
        logger.critical("Each column is missing the following values: {}".format(missing_digits_columns))
        logger.critical("Each grid is missing the following values: {}".format(missing_digits_grid))

        i = 0        # used to identify the row of the board
        j = 0        # used to identify the column of the board
        k = 1        # used to iterate through digits 1 through 9 like in a Sudoku game
        m = 0        # used to identify the element in missing_digits_rows
        p = 0        # used to identify the element of element m in missing_digits_rows

        for x in range(9):
            for y in range(9):
                for z in range(9):

                    logger.debug("Now testing the digit {} at row {} column {}".format(k, i+1, j+1))

                    # TODO: Is there an easier way to run this logic, or do I already know gridnum ?
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
                    # logger.debug("gridnum is equal to {}".format(gridnum))

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

                        # check if the first digit from our known missing values (grid) exists in our current row
                        if k in missing_digits_grid[gridnum-1]:
                            # this means digit "k" lives in the grid
                            missing_from_grid = True

                        if missing_from_row and missing_from_column and missing_from_grid:
                            logger.warning("Digit {} could potentially live in row {} column {}".format(k, i + 1, j + 1))
                            potential_solutions[cell_value].append(str(k))
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

        for w in potential_solutions:
            if len(w) == 1:
                logger.info("We can fill in the empty cell {} with the value {}".format(potential_solutions.index(w)+1, w))
                # Append value to board
                board_row = (potential_solutions.index(w) + 1) / 9
                board_row = math.ceil((potential_solutions.index(w)+1) / 9)
                board_column = (potential_solutions.index(w)+1) % 9

                if board_column == 0:
                    board_column = 9

                logger.warning("Replacing the empty value in row {} column {} with a {}".format(board_row, board_column, w[0]))
                board[board_row - 1][board_column - 1] = w[0]

        return board

    b = 0
    for row in board:
        while "." in row:
            logger.critical("**********************************************************************")
            logger.warning("Find the missing digits in each row of the Sudoku board")
            # Creates a list of lists
            missing_digits_rows = find_missing_digits(board)
            logger.warning(
                "Transpose rows into columns so that we can find the missing digits in each column of the Sudoku board")
            change_rows_to_columns = transpose_rows_to_columns(board)
            logger.warning("Find the missing digits in each column of the Sudoku board")
            missing_digits_columns = find_missing_digits(change_rows_to_columns)
            change_grid_to_rows = create_lists_for_grids(board, change_rows_to_columns)
            missing_digits_grid = find_missing_digits(change_grid_to_rows)
            test_digits(board, missing_digits_rows, missing_digits_columns, missing_digits_grid)

            logger.debug("\n" + "New board value is:" + "\n" + "\n".join(str(h) for h in board))
            b += 1
        logger.warning("ran this {} times".format(b))

    # logger.critical(board)
    logger.critical("\n" + "New board value is:" + "\n" + "\n".join(str(h) for h in board))

    # TODO: Is there something we can do with the information of "X digit CANNOT live in row..." ?

    # TODO: Calculate the number that the missing digits of each row must add up to equal
    # def sum_row_value(self):
        # In the case of a 9x9, that number is 45

    # TODO: Calculate the number that the missing digits of each column must add up to equal
    # def sum_column_value(self):
        # In the case of a 9x9, that number is 45



