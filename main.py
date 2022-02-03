from tkinter import *
from BoardVisual import *
from Board import *
from StartGame import *
from Sack import *
from Player import *
from BoardVisual import *
from GameController import *
from Letters import *


class Main:

    def __init__(self):
        """
            Constructor of Main class.
                sack:(Sack) representation of bag of letters
                root:(Tk) tkinter root
                startframe:(Frame) tkinter Frame displayed when the game starts
                mainframe:(Frame) tkinter Frame
                displayed during the game with board,
                rack and functional buttons
                players:(list of Player) list of all the players representation
                num_of_players:(int) number of players
                startgame:(StartGame) object  needed to display the instruction
        """
        self.root = Tk()
        self.startframe = Frame(self.root)
        self.mainframe = Frame(self.root)
        self.num_of_players = 2
        self.players = []
        self.sack = Sack()
        self.startgame = StartGame()
        self.root.title("Scrabble")
        self.root.geometry("1500x900")
        self.startframe.grid(column=0, row=0)
        startLabel = Label(self.startframe, text="Welcome to Scrabble!")
        startLabel.grid(column=3, row=0)
        startButton = Button(self.startframe, text="New game",
                             command=lambda: Main.getNumofPlayers(self))
        startButton.grid(column=3, row=5)
        instrButton = Button(self.startframe, text="See the instruction",
                             command=lambda: Main.getInstr(self))
        instrButton.grid(column=3, row=8)

    def getInstr(self):
        """
                This function creates a window
                where the instruction is displayed
                :return: void - only displays text
        """
        instrWindow = Toplevel()
        view_instr = self.startgame.viewInstruct()
        instrMsg = Message(instrWindow, text=view_instr)
        instrMsg.grid(column=1, row=1)
        closeInstrButton = Button(instrWindow, text="Ok, I get it",
                                  command=instrWindow.destroy)
        closeInstrButton.grid(column=3, row=3)

    def getNumofPlayers(self):
        """
                    This function creates a window where
                    you can choose the number of players
                    :return: void - only creating tkinter wigets
        """
        def num_of_PL(txt):
            # save number of players
            self.num_of_players = txt

        num_of_plWindow = Toplevel()
        num_of_playersL = Label(num_of_plWindow,
                                text="Choose number of players:")
        num_of_playersL.grid(column=1, row=1)
        for i in range(2, 5):
            numButton = Button(num_of_plWindow, text=str(i),
                               command=lambda x=i: [num_of_PL(x),
                                                    num_of_plWindow.destroy(),
                                                    self.getNames()])
            numButton.grid(row=2, column=1 + i)

    def getNames(self):
        """
            This function creates a window where you can
            input player's names and save them
            :return: void - only creating tkinter wigets and saving names
        """

        def get_all_names(window):
            # read names from the input (window) and create Player objects
            children_widgets = window.winfo_children()
            for child_widget in children_widgets:
                if child_widget.winfo_class() == 'Entry':
                    self.players.append(Player(self.sack, 7,
                                               child_widget.get()))

        nameWindow = Toplevel()
        infoLabel = Label(nameWindow, text="Input names:")
        infoLabel.grid(row=1, column=1)
        for i in range(1, self.num_of_players+1):
            nameLabel = Label(nameWindow, text="Player nr "+str(i))
            nameLabel.grid(column=1, row=i+1)
            nameEntry = Entry(nameWindow)
            nameEntry.grid(column=2, row=i+1)

        # destroing startframe and going to mainframe with letsPlay method
        confirmB = Button(nameWindow, text="Confirm")
        confirmB["command"] = lambda: [get_all_names(nameWindow),
                                       nameWindow.destroy(),
                                       self.startframe.destroy(),
                                       Main.letsPlay(self)]
        confirmB.grid(column=3, row=3)

    def letsPlay(self):
        """
            Function for managing the game and the wigets
            :return: void - only creating tkinter wigets
        """

        b = [['' for columns in range(15)] for rows in range(15)]
        GameContr = GameController(self.root, self.mainframe,
                                   self.sack, self.players)
        board = BoardVisual(self.root, self.mainframe, b)
        board.draw_functional_buttons(self.mainframe, GameContr, self.players)


a = Main()
a.root.mainloop()
