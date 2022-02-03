from Letters import *
from random import shuffle


class Sack:
    """
        Sack class is a represenation of the sack (bag of letters)
    """

    def __init__(self):
        """
            Constructor of Sack class.
                sack:(list) list of letters available in the game
                bag:(Letters) Letters() object
                with attribute bag which is a dict where
                key: letter - val: [points you get for the letter,
                                    number of tiles in the bag]

        """
        self.sack = []
        self.bag = Letters()
        self.initialize()

    def initialize(self):
        """
                This function initializes the sack
                It adds each letter from the bag specified number of times
                :return: void - only changing the object
        """
        bag = self.bag.bag
        for elem in bag:
            for _ in range(bag[elem][1]):
                self.sack.append(elem)

    def leftLetters(self):
        """
                This function gives number of letters left in the sack
                :return: int -  number of letters left in the sack
        """
        return len(self.sack)

    def takeLetter(self):
        """
                This function gives random letter out of the sack.
                It uses shuffle to randomize the output
                :return: char - letter
        """
        shuffle(self.sack)
        return self.sack.pop()

    def getSack(self):
        """
                This function returns a sack.
                :return: list - sack
        """
        return self.sack

    def remove(self, letter):
        """
                This function removes letter from the sack.
                :param letter:(char) letter to remove
                :return: void - only changing the object
        """

        if letter in set(self.sack):
            self.sack.remove(letter)

    def append(self, letter):
        """
                This function append letter to the sack.
                :param letter:(char) letter to add
                :return: void - only changing the object
        """
        self.sack.append(letter)
