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

    def test_digits(board: list, missing_digits_rows, missing_digits_columns, missing_digits_grid):

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
                count_digits = listtest[1]  # number of digits that were modified

                if count_digits == 0:
                    logger.critical(
                        "********************No changes were made this cycle, so we are stopping the WHILE loop********************")
                    logger.debug("\n" + "THE BOARD WILL REMAIN AS BEFORE:".format(b + 1) + "\n" + "\n".join(
                        str(h) for h in old_board))
                    return missing_digits_rows, missing_digits_columns, missing_digits_grid, change_grid_to_rows

                logger.debug("\n" + "New board value is:" + "\n" + "\n".join(str(h) for h in new_board))
                b += 1
                logger.warning("Loop has run {} time(s)".format(b))

                # https://stackoverflow.com/questions/14914615/in-python-find-out-number-of-differences-between-two-ordered-lists
                # logger.critical("new board is {}".format(message))
                # logger.critical("newwwwwww board is {}".format((sum(1 for i, j in zip(old_board[0], board[0]) if i != j))))

                logger.critical("*************END************")

        return missing_digits_rows, missing_digits_columns, missing_digits_grid, change_grid_to_rows

    # if we start using this method, this means our logic that solves some puzzles did not solve all puzzles
    def find_single_cells(self, missing_digits_rows, missing_digits_columns, missing_digits_grid, grid_to_rows):

        i = 0
        j = 0
        k = 0       # Refers to the position in the new 'single cells' List of Lists
        v = 0
        rows_in_grid = 3
        columns_in_grid = 3
        single_cells = [[] for i in range(9)]
        descend_row = 0
        grid_num = 1

        logger.debug("(missing_digits_rows) Missing digits in each row: {}".format(missing_digits_rows))
        logger.debug("(missing_digits_columns) Missing digits in each column: {}".format(missing_digits_columns))
        logger.debug("(missing_digits_grid) Missing digits in each grid: {}".format(missing_digits_grid))
        logger.debug("Each grid's values: {}".format(grid_to_rows))

        # For each grid represented in grid_to_rows
        for grid in grid_to_rows:

            if grid_num % 3 == 1:
                j = 0
                if grid_num == 1:
                    i = 0
                if grid_num == 4:
                    i = 3
                if grid_num == 7:
                    i = 6
            # grid num 2, 5, 8
            elif grid_num % 3 == 2:
                j = 3
                if grid_num == 2:
                    i = 0
                if grid_num == 5:
                    i = 3
                if grid_num == 8:
                    i = 6
            # grid num 3, 6, 9
            elif grid_num % 3 == 0:
                j = 6
                if grid_num == 3:
                    i = 0
                if grid_num == 6:
                    i = 3
                if grid_num == 9:
                    i = 6

            # For each element in the row of grid_to_rows
            for cell_value in grid:
                # for descend_row in range(3):
                if cell_value == ".":
                    for element in missing_digits_grid[v]:
                        if element in missing_digits_rows[i] and element in missing_digits_columns[j]:
                            single_cells[k].append(element)
                    j += 1
                else:
                    single_cells[k].append("---")
                    j += 1
                descend_row += 1
                k += 1
                if descend_row % 3 == 0:
                    i += 1
                    # ********************** ALERT THIS WAS THE ORIGINAL J VALUE *************************
                    # j = 0
                    j = j - 3
            v += 1
            k = 0
            digits_to_verify = []
            # TODO: Now must go through 'single_cells' and see how many instances of each digit occur. If only 1, then that digit has to be the answer
            for check_digit in range(1, 10):
                if str(check_digit) not in grid:
                    digits_to_verify.append(check_digit)

            tempcount = 0
            append_to_board = [[] for i in range(9)]
            close_flag = False
            t = 0

            # iterates through the numbers that have not yet been placed on grid number "grid_num"
            for now_check_digit in digits_to_verify:
                # iterates through the positions of grid number "grid_num"
                for singlecell in single_cells:
                    tempcount = tempcount + singlecell.count(now_check_digit)
                    if tempcount > 1:
                        tempcount = 0
                        # logger.warning("More than 1 possibility for digit {}".format(now_check_digit))
                        break
                if tempcount == 1:
                    logger.critical("WE HAVE A WINNER")
                    for find_winner in single_cells:
                        if now_check_digit in find_winner:
                            element_position_within_grid = single_cells.index(find_winner)

                            position_number = ((grid_num - 1) * 9) + single_cells.index(find_winner) + 1
                            logger.critical("The digit we get to insert is: {} at position {}".format(now_check_digit,
                                                          position_number))
                            logger.critical("The position within grid # {} is {}".format(grid_num, element_position_within_grid))

                            # formula from Discord conversation is:
                            # x = row = (row position in the subgrid + (row position in the 3x3 main grid * 3)) + 1
                            # y = column = (column position in the 3x3 subgrid + (column position in the 3x3 main grid * 3)) + 1

                            # for 74
                            # x = row = (0 + (2 * 3)) + 1 = 7
                            # y = column = (1 + (2 * 3)) + 1 = 8

                            # For 43:
                            # x = row = (2 + (1 * 3)) + 1 = 6
                            # y = column = (0 + (1 * 3)) + 1 = 4

                            if 0 <= element_position_within_grid <= 2:
                                subgrid_row = 0
                            elif 3 <= element_position_within_grid <= 5:
                                subgrid_row = 1
                            elif 6 <= element_position_within_grid <= 8:
                                subgrid_row = 2

                            if element_position_within_grid % 3 == 0:
                                subgrid_column = 0
                            elif element_position_within_grid % 3 == 1:
                                subgrid_column = 1
                            elif element_position_within_grid % 3 == 2:
                                subgrid_column = 2

                            if 1 <= grid_num <= 3:
                                maingrid_row = 0
                            elif 4 <= grid_num <= 6:
                                maingrid_row = 1
                            elif 7 <= grid_num <= 9:
                                maingrid_row = 2

                            if grid_num % 3 == 1:
                                maingrid_column = 0
                            elif grid_num % 3 == 2:
                                maingrid_column = 1
                            elif grid_num % 3 == 0:
                                maingrid_column = 2

                            position_number_row = (subgrid_row + (maingrid_row * 3)) + 1
                            position_number_column = (subgrid_column + (maingrid_column * 3)) + 1

                            logger.critical("Row to be modified: {} & Column to be modified: {}".format(position_number_row, position_number_column))
                            logger.critical(board)

                            append_to_board[t].append(position_number_row)
                            append_to_board[t].append(position_number_column)
                            append_to_board[t].append(now_check_digit)

                            close_flag = True
                            t += 1

                            break
                    else:
                        continue
            if close_flag == True:
                # delete the empty lists that were not filled
                del append_to_board[t:len(append_to_board)]

                return append_to_board

            # Before moving on to the next grid, check to see if any values in
            for check_singles in single_cells:
                if len(check_singles) == 1 and check_singles[0] != "---":
                    # We want to append this value to the main board
                    logger.critical("WRITE CODE TO ADD THIS VALUE TO THE CORRECT SPOT ON THE BOARD")
            logger.debug("Completed verifying digits with one home in 3x3 Grid #{}".format(v))
            # descend_row = 0

            single_cells = [[] for i in range(9)]
            grid_num += 1

testclass = LC_37()
everything = LC_37.check_changes(testclass, board)
# logger.critical(everything)

missing_digits_in_rows = everything[0]
missing_digits_in_columns = everything[1]
missing_digits_in_grid = everything[2]
grid_to_rows = everything[3]

append_to_board = LC_37.find_single_cells(testclass, missing_digits_in_rows, missing_digits_in_columns, missing_digits_in_grid, grid_to_rows)
logger.critical(append_to_board)
for appended in append_to_board:
    logger.warning("\n" + "Before:" + "\n" + "\n".join(
        str(h) for h in board))
    logger.warning(board[appended[0]-1][appended[1]-1])
    logger.warning("Modify row: {}".format(appended[0]))
    logger.warning("Modify column: {}".format(appended[1]))
    logger.warning("Insert number: {}".format(appended[2]))
    board[appended[0] - 1][appended[1] - 1] = str(appended[2])
    logger.warning("\n" + "After:" + "\n" + "\n".join(
        str(h) for h in board))

# TODO: Once the above values are appended to the board, then run the main logic again (hopefully this will solve the stalling)
remaining_missing_digits = LC_37.check_changes(testclass, board)
logger.critical(remaining_missing_digits)
logger.critical(board)


########################## FIRST LOGIC ##########################
testclass = LC_37()
everything = LC_37.check_changes(testclass, board)
# logger.critical(everything)

missing_digits_in_rows = everything[0]
missing_digits_in_columns = everything[1]
missing_digits_in_grid = everything[2]
grid_to_rows = everything[3]

########################## SECOND LOGIC ##########################
append_to_board = LC_37.find_single_cells(testclass, missing_digits_in_rows, missing_digits_in_columns, missing_digits_in_grid, grid_to_rows)
logger.critical(append_to_board)
for appended in append_to_board:
    logger.warning("\n" + "Before:" + "\n" + "\n".join(
        str(h) for h in board))
    logger.warning(board[appended[0]-1][appended[1]-1])
    logger.warning("Modify row: {}".format(appended[0]))
    logger.warning("Modify column: {}".format(appended[1]))
    logger.warning("Insert number: {}".format(appended[2]))
    board[appended[0] - 1][appended[1] - 1] = str(appended[2])
    logger.warning("\n" + "After:" + "\n" + "\n".join(
        str(h) for h in board))

########################## FIRST LOGIC ##########################
testclass = LC_37()
everything = LC_37.check_changes(testclass, board)
# logger.critical(everything)

missing_digits_in_rows = everything[0]
missing_digits_in_columns = everything[1]
missing_digits_in_grid = everything[2]
grid_to_rows = everything[3]

########################## SECOND LOGIC ##########################
append_to_board = LC_37.find_single_cells(testclass, missing_digits_in_rows, missing_digits_in_columns, missing_digits_in_grid, grid_to_rows)
logger.critical(append_to_board)


try:
    for appended in append_to_board:
        logger.warning("\n" + "Before:" + "\n" + "\n".join(
        str(h) for h in board))
        logger.warning(board[appended[0]-1][appended[1]-1])
        logger.warning("Modify row: {}".format(appended[0]))
        logger.warning("Modify column: {}".format(appended[1]))
        logger.warning("Insert number: {}".format(appended[2]))
        board[appended[0] - 1][appended[1] - 1] = str(appended[2])
        logger.warning("\n" + "After:" + "\n" + "\n".join(str(h) for h in board))
except Exception:
    pass


#####################################################################
# https://sudoku9x9.com/howtosolve.php
'''
In rows R1, R4 and R8, only cells in columns C1, C2 and C8 may have digit "5" as a candidate. Therefore, within each of 
these 3 columns, "5" must reside in one of the cells in rows R1, R4 and R8 and cannot be possibilities for cells in other rows.
'''
# TODO: Attempt to write logic for the reasoning above ^^^

# log the position of each row for any missing digits in that row
def cell_possibilities(board, missing_digits_in_rows, missing_digits_in_columns, missing_digits_in_grid):

    possible_solutions = [[] for i in range(81)]
    i = 0   # indicates the row number of board
    j = 0   # indicates the column number of board
    p = 0   # indicates the element within the 'missing' lists I am checking
    grid_num = 1
    count = 0   # will be used to keep track of the 81 positions of possibilities

    #TODO: How do you calculate grid_num ?

    # Answer from Discord
    # grid_num = 3 * (i // 3) + (j // 3) + 1

    # if 1 <= i <= 3:
    #     if 1 <= j <= 3: grid_num = 1
    #     if 4 <= j <= 6: grid_num = 2
    #     if 7 <= j <= 9: grid_num = 3
    # if 4 <= i <= 6:
    #     if 1 <= j <= 3: grid_num = 4
    #     if 4 <= j <= 6: grid_num = 5
    #     if 7 <= j <= 9: grid_num = 6
    # if 7 <= i <= 9:
    #     if 1 <= j <= 3: grid_num = 7
    #     if 4 <= j <= 6: grid_num = 8
    #     if 7 <= j <= 9: grid_num = 9

    # Add all valid possibilities to the cell
    for rows in board:
        # Check rows
        for missing in missing_digits_in_rows:

            for y in range(9):
                grid_num = 3 * (i // 3) + (j // 3) + 1
                logger.debug(
                    "Currently checking missing {} in row {} column {} in grid {}".format(missing, i + 1, j + 1, grid_num))

                for x in range(len(missing)):

                    if rows[j] != '.':
                        logger.info("row {} column {} in grid {} is already filled in".format(i + 1, j + 1, grid_num))
                        possible_solutions[count].append("Full")
                        break

                    miss = missing[p]
                    col = missing_digits_in_columns[j]
                    grid = missing_digits_in_grid[grid_num-1]

                    if miss in col and missing[p] in grid:
                        possible_solutions[count].append(missing[p])

                    p += 1
                logger.warning(
                    "Finished filling in missing values for row {} column {} in grid {}".format(i + 1, j + 1, grid_num))
                p = 0
                count += 1
                j += 1

            j = 0
            i += 1
        if i >= 9:
            break
    logger.debug("All possible solutions filled in: {}".format(possible_solutions))


cell_possibilities(board, missing_digits_in_rows, missing_digits_in_columns, missing_digits_in_grid)
logger.debug(board)
logger.critical("\n" + "Currently, the board is:" + "\n" + "\n".join(
                    str(h) for h in board))







