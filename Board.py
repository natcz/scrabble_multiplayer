class Board:
    """
        Board class is a representation of the board
        on which the game takes place
    """

    def __init__(self, size):
        """
          Constructor of Board class.
              :param size:(int) size of the board (length of columns and rows)
              board: (list of lists) representation of the board

        """
        self.size = size
        self.board = [['_' for columns in range(size)] for rows in range(size)]

    def boardUpdate(self, new_word, coords):
        """
            This function adds new word on to the board
            :param new_word:(string) word which the player
                                        wants to add to the board
            :param coords:(collections defaultdict)
                        key: coordinates of the letter (x,y)
                        val: letter
                :return: void - only changing the object
        """

        nw = new_word.upper()
        for i in range(len(coords)):
            x, y = coords[i]
            self.board[x][y] = nw[i]

    def getBoard(self):
        """
                This function returns the board
                :return: list - Board property board
        """
        return self.board
