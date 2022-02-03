
from tkinter import *
import db_actions
import db_players
from datetime import datetime


class EndGame:
    """
        EndGame class is used when the game is over

    """
    def __init__(self, players, root):
        """
            Constructor of EndGame class.
                :param players:(list of Player objects) list of players
                :param root:(Tk) tkinter root
        """
        self.players = players
        self.root = root

    def bestPlayer(self):
        """
                This function checks which player won
                :return: Player - player that won the game
        """
        return max(self.players, key=lambda p: p.getScore())

    def save_all_players(self):
        for player in self.players:
            player_db = db_players.Player(player_name=player.name,
                                          score=player.score)
            db_actions.save_player(player_db)

    def print_top_players(self, history):
        top_playersWindow = Toplevel()
        l = Label(top_playersWindow, text="TABLE OF WINNERS")
        top_playersTxt = Text(top_playersWindow)
        counter = 0
        text = "DATE  NAME  SCORE\n"
        top_playersTxt.insert('1.0', text)
        for record in history():
            if counter < 10:
                date = record.date
                pl_name, pl_score = record.player_name, record.score
                players = str(date)+" "+str(pl_name)+" "+str(pl_score)+"\n"
                top_playersTxt.insert('1.0', players)
                counter += 1
        exitB = Button(top_playersWindow, text="EXIT")
        exitB["command"] = lambda: top_playersWindow.destroy()
        exitB.grid(column=3, row=5)
        l.grid(column=2, row=1)
        top_playersTxt.grid(column=2, row=3)

    def print_last_game_scores(self, get_players):
        last_gameWindow = Toplevel()
        last_gameTxt = Text(last_gameWindow)

        text = "NAME  SCORE\n"
        last_gameTxt.insert('1.0', text)
        for record in get_players():
            pl_name, pl_score = record.player_name, record.score
            players = str(pl_name)+" "+str(pl_score)+"\n"
            last_gameTxt.insert('1.0', players)

        exitB = Button(last_gameWindow, text="EXIT")
        exitB["command"] = lambda: last_gameWindow.destroy()
        exitB.grid(column=3, row=5)
        last_gameTxt.grid(column=2, row=3)

    def endWindow(self):
        """
                This function makes window appear when the game is over.
                This window contains of a tkinter Message
                with the info about the winner
                and a tkinter button "EXIT"
                to end the game (which destroys tk root)
                You can also display top 10 winners
                and see scores of all of the players in this game.
                :return: void - changing the tkinter root
        """

        endWindow = Toplevel()      # creating a Toplevel window

        winner = self.bestPlayer()  # Player() object
        winner_db = db_players.History(player_name=winner.name,
                                       date=datetime.now(),
                                       score=winner.score)
        db_actions.save_winner(winner_db)
        self.save_all_players()

        endMsg = Message(endWindow, text="GAME OVER!\n" + "CONGRATULATIONS\n" +
                                         str(winner.name).upper())
        exitB = Button(endWindow, text="EXIT")
        exitB["command"] = lambda: [self.root.destroy(),
                                    db_players.delete_table(db_players.Player)]
        endMsg.grid(column=1, row=1)
        exitB.grid(column=2, row=4)

        winners_tableB = Button(endWindow, text="SEE WINNERS TABLE")
        winners_tableB["command"] = lambda: self.print_top_players(db_actions.get_history)
        winners_tableB.grid(column=2, row=3)

        lastgame_tableB = Button(endWindow, text="SEE SCORES\n"
                                                 "FROM LATEST GAME")
        lastgame_tableB["command"] = lambda: self.print_last_game_scores(db_actions.get_players)
        lastgame_tableB.grid(column=1, row=2)
