import logging
import Logging

Logging.logging_function()
logger = logging.getLogger(__name__)

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

    def sudoku_solver(board):
        board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                 [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                 ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                 [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                 [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        # TODO: Keys to solving a sudoku
        # 1) all rows / columns must add up to 45
        # 2) all rows / columns can only have each digit once
        # 3) search for any rows / columns with one missing space

        # TODO: Maybe start by calculating all possible values per row / column

        i = 1
        j = 0
        test = []

        # for x in range(len(board)):
        for y in range(len(board)):
            # remove periods?

            if str(i) not in board[0]:
                test.insert(j, i)
                # print(test)
                j = j + 1

            i = i + 1

        logger.info("Row 1 needs the numbers: ")
        logger.info(test)

        # column one would return 1,2,3,9

    sudoku_solver(1)

