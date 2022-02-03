from Rack import *
from Word import *


class Player:
    """
        Player class is a represenattion of the player
    """
    def __init__(self, sack, max_l, name):
        """
            Constructor of Player class.
                :param sack:(list) list of letters available in the game
                :param  max_l:(int) number of letters in player's rack
                :param name:(string) name of the player
                rack:(Rack) player's rack
                score:(int) player's score (starting with 0)


        """
        self.rack = Rack(sack, max_l)
        self.score = 0
        self.name = name

    def getScore(self):
        """
                This function returns player's score
                :return: (int) score
        """
        return self.score

    def incScore(self, word, coords):
        """
            This function increases player's score.
            :param word:(string) word player made up
            :param coords:(itertools deafaultdict)
            where key: coordinates of the letter (x,y) val: letter
            :return: void - only changing the object attribute
        """
        w = Word(word)
        # calculating score increase using Word() score method (it returns int)
        plus_scr = w.score(coords)
        self.score += plus_scr
