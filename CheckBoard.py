from Board import *
from Word import *


class CheckBoard:
    """
        CheckBoard class is a tool
        to check if the player's move was correct

    """
    def __init__(self, board):
        """
                Constructor of CheckBoard class.
                :param board:(list) board representation
        """
        self.board = board

    def checkRows(self, eng_dict):
        """
            This function checks if all of the words
            placed in rows of the board are in the eng_dict
            :param eng_dict:(set) english dictionary (set of english words)
            :return: boolean
        """

        board_size = len(self.board)
        row = 0
        while row < board_size:
            column = 0               # column (int)
            while column < board_size:
                if self.board[row][column] != '_':
                    new_word = ""
                    # searching for a whole word
                    for col in range(column, board_size):
                        if self.board[row][col] != '_':
                            new_word += self.board[row][col]
                        else:
                            # if we found whole word
                            if new_word and len(new_word) > 1:
                                nw = Word(new_word)
                                # we are checking if it's in the eng_dict set
                                if not nw.checkWord(eng_dict):
                                    return False
                            column += len(new_word)
                            break
                column += 1
            row += 1
        return True

    def checkColumns(self, eng_dict):
        """
                    This function checks if all of the words placed in columns
                                            of the board are in the eng_dict
                    :param eng_dict:(set) english dictionary
                    :return: boolean
        """

        board_size = len(self.board)
        column = 0
        while column < board_size:
            row = 0
            while row < board_size:
                if self.board[row][column] != '_':
                    new_word = ""
                    for r in range(row, board_size):  # searching for whol word
                        if self.board[r][column] != '_':
                            new_word += self.board[r][column]

                        else:
                            # if we found whole word
                            if new_word and len(new_word) > 1:
                                nw = Word(new_word)
                                # we are checking if it appears
                                # in the eng_dict set
                                if not nw.checkWord(eng_dict):
                                    return False
                            row += len(new_word)
                            break
                row += 1
            column += 1
        return True

    def checkBoard(self, eng_dict, word, coords):
        """
                    This function checks if you can place the word
                    with letter coordinates on the board.
                    It uses checkRows and checkColumns.

                    :param eng_dict:(set) English dictionary
                    :param word:(string) newly placed word
                    :param coords:(itertools defaultdictionary)
                            key: coordinates of the letter (x,y)
                            val: letter
                    :return: boolean
        """
        # temporary board on which we test the placing
        temp_board = Board(len(self.board))
        temp_board.board = self.board[:]

        try:
            # using board updating method from Board()
            temp_board.boardUpdate(word, coords)
            temp_board_check = CheckBoard(temp_board.board)
            if not temp_board_check.checkRows(eng_dict):
                return False
            elif not temp_board_check.checkColumns(eng_dict):
                return False
            else:
                return True

        except ValueError:
            return False
