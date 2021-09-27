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

board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]


class LC_37():

    # board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    #          [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    #          ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    #          [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    #          [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    # board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    # modified board 1 line above this with where it stalled out
    # board = [[".",".","9","7","4","8",".",".","."],["7",".",".","6",".","2",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],[".",".",".","8","6","3",".","2","."],[".",".",".","4","9","1",".",".","6"],[".",".",".","2","7","5","9",".","."]]

    logger.warning("\n" + "Board to be solved is:" + "\n" + "\n".join(str(h) for h in board))

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

            '''
            logger.debug("Grid #{} has Rows {} through {} and Columns {} through {}".format(
                        gridnum, starting_row_position, ending_row_position,
                        starting_column_position, ending_column_position))
            '''

            i = starting_row_position
            j = starting_column_position

            # create lists containing values of each grid
            for x in range(3):
                for y in range(3):
                    grid_elements[gridnum-1].append(row_list[i-1][j-1])
                    j += 1
                i += 1
                j = starting_column_position

        # logger.debug("Lists of 3x3 grids: {}".format(grid_elements))

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

        missing_from_row = False
        missing_from_column = False
        missing_from_grid = False

        # Debug the top level for loop only if you want to see the digits get populated throughout the 'potential_solutions' LIST
        for x in range(9):
            for y in range(9):
                '''
                logger.debug("Now testing the digit {} at row {} ".format(k, i + 1))
                '''

                for z in range(9):

                    '''
                    logger.debug("Now testing the digit {} at row {} column {}".format(k, i+1, j+1))
                    '''

                    # TODO: Is there an easier way to run this logic, or do I already know gridnum ?
                    # need to be able to identify what grid we are in at any point
                    if 1 <= i + 1 <= 3:
                        # this means we are in gridnum 1, 2, or 3
                        if 1 <= j + 1 <= 3:
                            gridnum = 1
                        elif 4 <= j + 1 <= 6:
                            gridnum = 2
                        elif 7 <= j + 1 <= 9:
                            gridnum = 3
                    elif 4 <= i + 1 <= 6:
                        # this means we are in gridnum 4, 5, or 6
                        if 1 <= j + 1 <= 3:
                            gridnum = 4
                        if 4 <= j + 1 <= 6:
                            gridnum = 5
                        if 7 <= j + 1 <= 9:
                            gridnum = 6
                    elif 7 <= i + 1 <= 9:
                        # this means we are in gridnum 7, 8, or 9
                        if 1 <= j + 1 <= 3:
                            gridnum = 7
                        if 4 <= j + 1 <= 6:
                            gridnum = 8
                        if 7 <= j + 1 <= 9:
                            gridnum = 9
                    else:
                        logger.critical("Something went wrong because gridnum is not equal to 1 through 9")
                    # logger.debug("gridnum is equal to {}".format(gridnum))

                    # if a spot on the board is blank
                    if board[i][j] == ".":
                        # logger.debug("Missing value at row {} column {}".format(i+1, j+1))

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
                            '''
                            logger.warning("Digit {} could potentially live in row {} column {}".format(k, i + 1, j + 1))
                            '''
                            potential_solutions[cell_value].append(str(k))
                            '''
                            logger.warning("Potential solutions are now: {}".format(potential_solutions))
                            '''
                        '''
                        else:
                            logger.warning("Digit {} CANNOT live in row {} column {}".format(k, i + 1, j + 1))
                        '''

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
        # logger.info("Potential solutions are: {}".format(potential_solutions))

        count_changes = 0
        for w in potential_solutions:
            if len(w) == 1:
                # This would mean there is only one solution for the given cell
                logger.warning("We can fill in the empty cell {} with the value {}".format(potential_solutions.index(w)+1, w))
                # Append value to board
                board_row = (potential_solutions.index(w) + 1) / 9
                board_row = math.ceil((potential_solutions.index(w)+1) / 9)
                board_column = (potential_solutions.index(w)+1) % 9

                if board_column == 0:
                    board_column = 9

                logger.warning("Replacing the empty value in row {} column {} with a {}".format(board_row, board_column, w[0]))
                board[board_row - 1][board_column - 1] = w[0]
                count_changes += 1
        logger.debug("{} changes were made this round".format(count_changes))

        return board, count_changes

    def check_changes(self, board):

        b = 0
        for row in board:
            while "." in row:
                old_board = board
                # count_digits = 0
                # logger.critical("old board is {}".format("\n" + "New board value is:" + "\n" + "\n".join(str(h) for h in board)))
                logger.critical("\n" + "Cycle #{} - Currently, the board is:".format(b + 1) + "\n" + "\n".join(
                    str(h) for h in old_board))

                logger.warning("Begin finding the missing digits in each ROW of the Sudoku board:")
                # asdfasdf = LC_37.find_missing_digits(board)
                missing_digits_rows = LC_37.find_missing_digits(board)
                logger.warning(
                    "Transpose rows into columns so that we can find the missing digits in each column of the Sudoku board")
                change_rows_to_columns = LC_37.transpose_rows_to_columns(board)

                logger.warning("Begin finding the missing digits in each COLUMN of the Sudoku board:")
                missing_digits_columns = LC_37.find_missing_digits(change_rows_to_columns)
                change_grid_to_rows = LC_37.create_lists_for_grids(board, change_rows_to_columns)

                logger.warning("Begin finding the missing digits in each 3x3 GRID of the Sudoku board:")
                missing_digits_grid = LC_37.find_missing_digits(change_grid_to_rows)
                listtest = LC_37.test_digits(board, missing_digits_rows, missing_digits_columns, missing_digits_grid)

                new_board = listtest[0]
                count_digits = listtest[1]

                if count_digits == 0:
                    logger.critical(
                        "********************No changes were made this cycle, so we are stopping the WHILE loop********************")
                    return missing_digits_rows, missing_digits_columns, missing_digits_grid

                logger.debug("\n" + "New board value is:" + "\n" + "\n".join(str(h) for h in new_board))
                b += 1
                logger.warning("Loop has run {} time(s)".format(b))

                # https://stackoverflow.com/questions/14914615/in-python-find-out-number-of-differences-between-two-ordered-lists
                # logger.critical("new board is {}".format(message))
                # logger.critical("newwwwwww board is {}".format((sum(1 for i, j in zip(old_board[0], board[0]) if i != j))))

                logger.critical("*************END************")

        return missing_digits_rows, missing_digits_columns, missing_digits_grid

    # if we start using this method, this means our logic that solves some puzzles did not solve all puzzles
    def find_single_cells(self, missing_digits_rows, missing_digits_columns, missing_digits_grid):

        i = 0
        j = 0
        rows_in_grid = 3
        columns_in_grid = 3

        # check to see if there is only one cell in each 3x3 grid that can legally have a digit
        for gridnum in range(9):
            # We can optimize this later to only iterate through the empty cells rather than all 9 cells
            for cell in range(9):
                for digit in missing_digits_grid:
                    # If the cell is blank, AND digit is not in the row, or column already
                    if board[i][j] == ".":
                        # if digit
                        break


testclass = LC_37()
everything = LC_37.check_changes(testclass, board)
logger.critical(everything)
missing_digits_in_rows = everything[0]
missing_digits_in_columns = everything[1]
missing_digits_in_grid = everything[2]
# logger.debug(missing_digits_in_rows)
# logger.debug(missing_digits_in_columns)
# logger.debug(missing_digits_in_grid)
LC_37.find_single_cells(testclass, missing_digits_in_rows, missing_digits_in_columns, missing_digits_in_grid)

    # TODO: Above code stalled out --- need to account for grids where a digit can only live in one of the 9 spots..

    # TODO: Is there something we can do with the information of "X digit CANNOT live in row..." ?

    # TODO: Calculate the number that the missing digits of each row must add up to equal
    # def sum_row_value(self):
        # In the case of a 9x9, that number is 45

    # TODO: Calculate the number that the missing digits of each column must add up to equal
    # def sum_column_value(self):
        # In the case of a 9x9, that number is 45



