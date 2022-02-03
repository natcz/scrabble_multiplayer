from tkinter import *
from Letters import *

BOARD_SIZE = 15


class BoardVisual:
    """
        BoardVisual class is a visualisation of the board
        on which the game takes place
        It mainly uses tkinter
        Every spot on the board is a tkinter button
    """

    def __init__(self, root, frame, board):
        """
                Constructor of BoardVisual class.
                    :param root:(Tk)
                    :param frame:(tkinter Frame)
                    :param board:(list) board representation
        """

        self.frame = frame
        self.root = root
        self.board = board
        self.initialize()
        self.frame.grid(row=5, column=5)

    def initialize(self):
        """
                This function initializes the view of the board
                It first creates number labels
                around the board using tkinter Label,
                then creates visualisation of the board itself
                using tkinter Buttons with no text on
                along with the special tiles or a center of the board
                (creating them with different colours and text on)
                :return: void - only changing
                        the object and putting it in the tk.Frame
        """

        global BOARD_SIZE
        # creating labels around the board

        for col in range(1, BOARD_SIZE + 1):
            label = Label(self.frame, text=str(col))
            label.grid(row=0, column=col)

        for row in range(1, BOARD_SIZE + 1):
            label = Label(self.frame, text=str(row))
            label.grid(row=row, column=0)

        # creating visualisation of the board itself
        for row in range(1, BOARD_SIZE + 1):
            for col in range(1, BOARD_SIZE + 1):
                tileButton = Button(self.frame, height=3,
                                    width=3, bg="bisque", fg="gray1", text=" ")
                tileButton.grid(row=row, column=col)
                self.board[row - 1][col - 1] = tileButton

        # special tiles
        self.board[7][7]["bg"] = "salmon"       # center of the board
        self.board[7][7]["text"] = "#"

        # LX means this place is a bonus place
        # (you get a bonus points if you place the letter on them)
        self.board[0][0]["bg"] = "light blue"
        self.board[0][0]["text"] = "L5"
        self.board[14][14]["bg"] = "light blue"
        self.board[14][14]["text"] = "L5"
        self.board[0][14]["bg"] = "light blue"
        self.board[0][14]["text"] = "L5"
        self.board[14][0]["bg"] = "light blue"
        self.board[14][0]["text"] = "L5"

        self.board[3][3]["bg"] = "pale green"
        self.board[3][3]["text"] = "L4"
        self.board[11][3]["bg"] = "pale green"
        self.board[11][3]["text"] = "L4"
        self.board[3][11]["bg"] = "pale green"
        self.board[3][11]["text"] = "L4"
        self.board[11][11]["bg"] = "pale green"
        self.board[11][11]["text"] = "L4"

        self.board[7][3]["bg"] = "pale violet red"
        self.board[7][3]["text"] = "L3"
        self.board[3][7]["bg"] = "pale violet red"
        self.board[3][7]["text"] = "L3"
        self.board[11][7]["bg"] = "pale violet red"
        self.board[11][7]["text"] = "L3"
        self.board[7][11]["bg"] = "pale violet red"
        self.board[7][11]["text"] = "L3"

        self.board[5][5]["bg"] = "plum2"
        self.board[5][5]["text"] = "L2"
        self.board[5][9]["bg"] = "plum2"
        self.board[5][9]["text"] = "L2"
        self.board[9][5]["bg"] = "plum2"
        self.board[9][5]["text"] = "L2"
        self.board[9][9]["bg"] = "plum2"
        self.board[9][9]["text"] = "L2"

    def draw_functional_buttons(self, mainframe, GameController, players):
        """
            Function responsible for drawing labels and functional buttons.
            Functional buttons:
                "HINT", "SKIP", "EXCHANGE ALL",
                "EXCHANGE ONE", "END MOVE", "UNDO MOVE"
            and labels:
                turn label, score label, information about points for letters
            and visualisation of the player's rack.
            :param mainframe:(tkinter Frame)
            :param GameConroller:(GameController)
            :param players:(list of Players objects)

        """
        # just for good placing
        emptyLabel = Label(mainframe, text="     ").grid(column=19, row=1)
        # displaying who's turn it is and the score
        TurnLabel = Label(mainframe,
                          text="IT'S " + str(players[0].name).upper() + "'S TURN")
        PScoreLabel = Label(mainframe,
                            text=str(players[0].name).upper() + "'S SCORE:")
        ScoreLabel = Label(mainframe, text=str(players[0].score))
        TurnLabel.grid(column=20, row=2)
        PScoreLabel.grid(column=20, row=3)
        ScoreLabel.grid(column=21, row=3)

        # displaying info about points for letters (letter=points)
        infoL = Label(mainframe, text="POINTS\n"
                                      "FOR LETTERS:")
        infoL.grid(column=30, row=1)
        letters = Letters()
        bag = letters.bag
        i = 0  # for good placing
        for letter, val in bag.items():
            if i <= 12:
                LettersL = Label(mainframe, text=str(letter) + " = " + str(val[0]) + "   ")
                LettersL.grid(column=31, row=2+i)

            else:
                LettersL = Label(mainframe, text=str(letter) + " = " + str(val[0]))
                LettersL.grid(column=32, row=2 + i-13)
            i += 1

        PlayerRackB = []  # buttons representing player's rack
        playerRack = players[0].rack.getRack()

        emptyL2 = Label(mainframe, text="    ").grid(column=22, row=1)  # just for placing

        # functional buttons
        skipB = Button(mainframe, text="SKIP", width=12)
        skipB["command"] = lambda: GameController.skip(PScoreLabel, ScoreLabel, TurnLabel,
                                                       PlayerRackB, undo_moveB, endMoveButton)

        undo_moveB = Button(mainframe, text="UNDO MOVE", width=12, state="disabled")
        undo_moveB["command"] = lambda: GameController.undoMove(self.board, PlayerRackB,
                                                                undo_moveB, endMoveButton)

        exchangeAllB = Button(mainframe, text="EXCHANGE ALL", width=12)
        exchangeAllB["command"] = lambda: GameController.exchangeAll(PlayerRackB)

        exchangeOneB = Button(mainframe, text="EXCHANGE ONE", width=12)
        exchangeOneB["command"] = lambda: GameController.exchangeOne(self.board, PlayerRackB,
                                                                     exchangeAllB, exchangeOneB,
                                                                     skipB, undo_moveB,
                                                                     endMoveButton)

        hintButton = Button(mainframe, text="HINT", width=12, state="disabled")
        hintButton["command"] = lambda: GameController.hint(self, PScoreLabel,
                                                            ScoreLabel, TurnLabel, PlayerRackB,
                                                            undo_moveB, endMoveButton)

        endMoveButton = Button(mainframe, text="END MOVE", width=12, state="disabled")
        endMoveButton["command"] = lambda: GameController.endTurn(PScoreLabel, ScoreLabel,
                                                                  TurnLabel,
                                                                  PlayerRackB, self.board,
                                                                  hintButton, exchangeAllB,
                                                                  exchangeOneB, skipB,
                                                                  undo_moveB,
                                                                  endMoveButton)
        skipB.grid(column=20, row=7)
        exchangeAllB.grid(column=20, row=8)
        exchangeOneB.grid(column=20, row=9)
        hintButton.grid(column=20, row=10)
        endMoveButton.grid(column=20, row=11)
        undo_moveB.grid(column=20, row=12)
        # visualizing the rack
        for i in range(len(playerRack)):
            button = Button(mainframe, height=3, width=3,
                            bg="bisque", fg="gray1", text=str(playerRack[i]))
            button.grid(column=23+i, row=9)
            PlayerRackB.append(button)

        # enable letters (buttons) to be moved to the board
        for i in range(len(PlayerRackB)):
            PlayerRackB[i]["command"] = lambda x=i: GameController.makeMove(x,
                                                                            self.board,
                                                                            PlayerRackB,
                                                                            exchangeAllB,
                                                                            exchangeOneB,
                                                                            skipB,
                                                                            undo_moveB,
                                                                            endMoveButton)
