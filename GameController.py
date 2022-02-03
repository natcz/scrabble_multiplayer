import copy

from Rack import *
from Board import *
from Letters import *
from tkinter import *
from CheckBoard import *
from collections import defaultdict as dd
from Word import *
from EndGame import *
from Hint import *

# global variables
turn = 0  # number of turns
good_first_word = False  # information about first move on the board success
# deafaultdict where key: coordinates of the letter (x,y) val: letter
Wcoordinates = dd()
coord = []  # coordinates of letters in the current placing word list of (x,y)
l = Letters()
eng_dict = l.makeDict()  # english dictionary set
demoBoard = Board(15)  # board
rack_indx = dd()  # deafultdict where key:letter    val:index in the rack


class GameController:
    """
        GameController class is kind of a backend tool.
        It manages all the functional buttons and moves of the players.
    """

    def __init__(self, root, frame, sack, players):
        """
                Constructor of GameController class.
                    :param root:(Tk) tkinter root
                    :param frame:(Frame) main frame with all the wigets
                    :param players:(list of Player) list of all the Players
                    :param number_of_players:(int) number of players
                    :param sack:(Sack) bag of letters

        """

        self.root = root
        self.sack = sack
        self.frame = frame
        self.players = players
        self.number_of_players = len(players)

    def skip(self, scrLabel, scrL, turnLabel,
             rackButtons, undoButton, endMoveButton):
        """
            This function is responsible of
            what happens when player hits the button SKIP
             :param rackButtons: (list) list of tk buttons aka player's rack
             :param turnLabel:(Label) displays who's turn it is
             :param scrL:(Label) displays score
             :param scrLabel:(Label) displays score


            :return: void - changing the turn (changing wigets)
        """
        undoButton["state"] = "disabled"
        endMoveButton["state"] = "disabled"
        for player in self.players:
            player.rack.fillRack()

        global turn

        turn += 1
        current_player = self.players[turn % self.number_of_players]
        scrLabel["text"] = str(current_player.name).upper() + "'S SCORE:"
        scrL["text"] = str(current_player.score)
        turnLabel["text"] = "IT'S " + str(current_player.name).upper() + "'S TURN"
        playerRack = current_player.rack.getRack()
        for i in range(len(rackButtons)):
            rackButtons[i]["text"] = str(playerRack[i])

    def exchangeAll(self, rackButtons):
        """
                This function is responsible of what happens
                 when player hits the button EXCHANGE ALL
                :param rackButtons: (list) list of tk buttons aka player's rack
                :return: void - changing the tiles in the rack
        """
        global turn

        current_player = self.players[turn % self.number_of_players]
        current_player.rack.exchangeAll()  # Rack() method
        playerRack = current_player.rack.getRack()
        for i in range(len(rackButtons)):
            rackButtons[i]["text"] = str(playerRack[i])

    def exchangeOne(self, board, rackButtons,
                    exAllButton, exOneButton,
                    skipButton, undoButton, endMoveButton):
        """
            This function is responsible of what happens
            when player hits the button EXCHANGE ONE
            :param rackButtons: (list) list of tk buttons aka player's rack
            :param board:(Board) representation of the board
            :param exAllButton:(Button) tkinter button to exchange all letters
            :param exOneButton:(Button) tkinter button to exchange one letter
            :param skipButton:(Button) tkinter button to skip the turn
            :return: void - changing one letter from the rack (changing wigets)
        """
        global turn

        current_player = self.players[turn % self.number_of_players]

        def exOne(button, ind):
            new_letter = current_player.rack.exchangeOne(ind)   # Rack() method
            button["text"] = str(new_letter).upper()

        def disableB(self, buttons):     # disable buttons
            for i in range(len(buttons)):
                buttons[i]["command"] = lambda x=i: self.makeMove(x, board,
                                                                  rackButtons,
                                                                  exAllButton,
                                                                  exOneButton,
                                                                  skipButton,
                                                                  undoButton,
                                                                  endMoveButton)

        for i in range(len(rackButtons)):
            rackButtons[i].config(command=lambda x=i: [exOne(rackButtons[x], x),
                                                       disableB(self, rackButtons)])

    def makeMove(self, ind, board, rackButtons, exAllButton,
                 exOneButton, skipButton, undoButton, endMoveButton):
        """
                This function is responsible of making the move,
                placing the letter onto the board
                :param ind: index of the letter in the rack
                :param rackButtons: (list) list of tk buttons aka player's rack
                :param board:(Board) representation of the board
                :param exAllButton:(Button) tk button to exchange all letters
                :param exOneButton:(Button) tk button to exchange one letter
                :param skipButton:(Button) tk button to skip the turn
                :return: void - changing one letter from the rack
        """
        global rack_indx
        global turn

        current_player = self.players[turn % self.number_of_players]

        def placeLetter(button, row, col, letter):
            global coord
            global Wcoordinates
            button["text"] = str(letter).upper()
            Wcoordinates[(row, col)] = letter
            coord.append((row, col))
        # getting the letter out of the player's rack

        letter = current_player.rack.getRack()[ind]
        rack_indx[letter] = ind

        # enable to place the letter (board tile text changing into letter)
        for row in range(15):
            for col in range(15):
                b_place = board[row][col]
                b_place["command"] = lambda c=col, r=row: placeLetter(board[r][c],
                                                                      r,
                                                                      c,
                                                                      letter)
        # disable other functionalities
        rackButtons[ind]["state"] = "disabled"
        exAllButton["state"] = "disabled"
        exOneButton["state"] = "disabled"
        skipButton["state"] = "disabled"
        undoButton["state"] = "normal"
        endMoveButton["state"] = "normal"

    def undoMove(self, board, rackButtons, undoButton, endMoveButton):
        """
                This function is responsible of what happens
                when player makes the wrong move
                :param rackButtons: (list) list of tk buttons akaplayer's rack
                :param board:(Board) representation of the board
                :param coords:(list) list of coordinates

                :return: void -  changing wigets
        """
        global demoBoard
        global turn
        global coord
        global Wcoordinates

        for i in range(len(coord)):    # letters out of the board
            board[coord[i][0]][coord[i][1]]["text"] = " "
            demoBoard.board[coord[i][0]][coord[i][1]] = "_"
        for i in range(len(rackButtons)):
            rackButtons[i]["state"] = "normal"
        undoButton["state"] = "disabled"
        endMoveButton["state"] = "disabled"
        coord = []
        Wcoordinates = dd()

    def makeProperWord(self):
        """
                This function makes word from letters
                placed in current turn on the board
                :return: string - word
        """

        global Wcoordinates, coord, turn

        sameRow = True
        sameCol = True
        c = coord[0][1]
        r = coord[0][0]
        word = ""
        for pair in coord:  # checking if letters are in the same column or row
            if pair[0] != r:
                sameRow = False
            if pair[1] != c:
                sameCol = False
        if not sameRow and not sameCol:
            return ""
        elif sameRow:  # all the letters in the same row
            coord.sort(key=lambda x: x[1])
            for pair in coord:
                word += Wcoordinates[pair]
            return word
        else:          # all the letters in the same column
            coord.sort()
            for pair in coord:
                word += Wcoordinates[pair]
            return word

    def endTurn(self, scrLabel, scrL, turnLabel,
                rackButtons, visualB, hintButton,
                exAllButton, exOneButton, skipButton,
                undoButton, endMoveButton):
        """
            This function is responsible
            of what happens when player hits "END TURN" button
            :param rackButtons: (list) list of tk buttons aka player's rack
            :param exAllButton:(Button) tk button to exchange all letters
            :param exOneButton:(Button) tk button to exchange one letter
            :param skipButton:(Button) tk button to skip the turn
            :param hintButton:(Button) tk button to get a hint
            :param visualB: (BoardVisual) board visualization
            :param turnLabel:(Label) displays who's turn it is
            :param scrL:(Label) displays score
            :param scrLabel:(Label) displays score
            :return: void -  changing wigets
        """
        global coord, eng_dict, rack_indx, turn
        global Wcoordinates, demoBoard, good_first_word
        current_player = self.players[turn % self.number_of_players]
        demolist = demoBoard.getBoard()
        checkB = CheckBoard(demolist[:])
        proper_word = self.makeProperWord()
        w = Word(proper_word)

        for i in range(len(rackButtons)):  # enable rack buttons
            rackButtons[i]["state"] = "normal"

        if turn == 0 or not good_first_word:   # first word on the board

            if coord[0] == (7, 7):    # checking special placing
                if w.checkWord(eng_dict):
                    board_ok = True
                    good_first_word = True
                else:
                    board_ok = False  # true if placing the word is possible
            else:
                board_ok = False
        else:
            board_ok = checkB.checkBoard(eng_dict, proper_word, coord)

        if board_ok:  # proper move
            demoBoard.boardUpdate(proper_word, coord)
            for xy in coord:
                l = Wcoordinates[xy]
                current_player.rack.remove(l)
                ind = rack_indx[l]
                rackButtons[ind]["text"] = " "
            current_player.incScore(proper_word, Wcoordinates)

        else:  # not a proper move
            bad_wordWindow = Toplevel()

            fail_msg = Message(bad_wordWindow,
                               text="Not a proper move " +
                                    str(current_player.name).upper() +
                                    ". You've lost your chance")

            fail_msg.grid(row=1, column=1)
            ok_Button = Button(bad_wordWindow, text="OK",
                               command=lambda: bad_wordWindow.destroy())
            ok_Button.grid(row=2, column=2)
            self.undoMove(visualB, rackButtons, undoButton, endMoveButton)

        if self.sack.sack == [] or current_player.score >= 15:
            # game is over
            self.endGame()

        Wcoordinates = dd()
        coord = []
        rack_indx = dd()

        # refilling the rack
        current_player.rack.fillRack()

        exAllButton["state"] = "normal"
        exOneButton["state"] = "normal"
        skipButton["state"] = "normal"
        if good_first_word:
            hintButton["state"] = "normal"
        undoButton["state"] = "disabled"
        # next turn
        self.skip(scrLabel, scrL, turnLabel,
                  rackButtons, undoButton, endMoveButton)

    def hint(self, visualB, scrLabel,
             scrL, turnLabel, rackButtons,
             undoButton, endMoveButton):
        """
                This function finds hint using Hint class method
                :return:void - displaying hint and placing it on the board
        """
        global turn
        current_player = self.players[turn % self.number_of_players]
        demolist = demoBoard.getBoard()
        prev_board = copy.deepcopy(demoBoard)  # copy in case of no hint

        h = Hint(demolist, eng_dict, current_player.rack.getRack())
        word, w_coord = h.findHint()

        if word != "":   # found hint

            def apply_hint():

                for i in range(len(w_coord)):
                    visualB.board[w_coord[i][0]][w_coord[i][1]]["text"] = word[i]
                    current_player.rack.remove(word[i])

            hint_window = Toplevel()
            hint_msg = Message(hint_window)
            hint_msg["text"] = "HINT: " + str(word).upper()
            hint_msg.grid(column=1, row=1)
            apply_hint_button = Button(hint_window, text="OK, APPLY HINT")
            apply_hint_button.grid(column=2, row=2)
            apply_hint_button["command"] = lambda: [apply_hint(),
                                                    hint_window.destroy(),
                                                    self.skip(scrLabel,
                                                              scrL,
                                                              turnLabel,
                                                              rackButtons,
                                                              undoButton,
                                                              endMoveButton)]
            decline_hint_button = Button(hint_window,
                                         text="CLOSE AND DO NOT APPLY HINT")
            decline_hint_button.grid(column=2, row=4)

            def prev_b():
                demoBoard.board = prev_board.board

            decline_hint_button["command"] = lambda: [hint_window.destroy(), prev_b()]

        else:  # no hint founded
            demoBoard.board = prev_board.board
            hint_window = Toplevel()
            hint_msg = Message(hint_window,
                               text="NO PROPER MOVE FOUND")
            hint_msg.grid(column=1, row=1)
            close_button = Button(hint_window, text="OK")
            close_button.grid(column=2, row=2)
            close_button["command"] = lambda: hint_window.destroy()

    def endGame(self):
        """
                This function is responsible
                for what happens when the game ends
                :return: void - displaying endWindow
        """
        endG = EndGame(self.players, self.root)
        endG.endWindow()
