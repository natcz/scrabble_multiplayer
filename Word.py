from random import shuffle
from Letters import *


class Word:
    """
        Word class is a representation of a singe word

    """
    def __init__(self, word):
        """
            Constructor of Word class.
            :param word:(string) representation of the word
            bag:(Letter) object with attribute bag which is a dict
            where  key: letter - val: (list)[points you get for the letter,
                                             number of tiles in the bag]

        """
        self.bag = Letters()
        self.word = word

    def checkWord(self, eng_dict):
        """
            This function checks if the word is in the english dictionary
            :param eng_dict:(set) english dictionary
            :return: boolean
        """
        return self.word in eng_dict

    def score(self, coords):
        """
            This function calculates the score player gets for his move
            :param coords:(itertools deafaultdict)
            where key: coordinates of the letter (x,y) val: letter
            :return: int - score
        """

        scr = 0
        for xy, letter in coords.items():
            points_for_letter = self.bag.bag[letter][0]
            scr += points_for_letter * self.bonusPoints(xy)
        return scr

    def bonusPoints(self, xy):
        """
                This function calculates bonus score for the letter
                :param xy:(tuple) coordinates of the letter on the board
                :return: int - score
        """
        # multA is a pair of coordinates (x,y)
        # on which you get a bonus A*points for letter
        mult3 = {(7, 3), (3, 7), (7, 11), (11, 7)}
        mult2 = {(5, 5), (9, 9), (5, 9),
                 (9, 5)}
        mult4 = {(3, 3), (11, 3), (3, 11), (11, 11)}
        mult5 = {(0, 0), (14, 14), (0, 14), (14, 0)}

        if xy in mult3:
            return 3
        elif xy in mult2:
            return 2
        elif xy in mult4:
            return 4
        elif xy in mult5:
            return 5
        return 1  # neutral element of multiplication
