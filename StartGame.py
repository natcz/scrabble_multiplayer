

class StartGame:
    """
        StartGame class is used when the game starts

    """

    def __init__(self):
        """
                Constructor of StartGame class.

                instruction:(string) instruction of the game


        """
        self.instruction = """
                           Welcome to Scrabble!\n
                           Scrabble is a board multiplayer game \n
                           Each of the players will get 7 random letters from
                           the Bag. They need to make up
                           the word with these and the ones\n
                           already on the board. To make your move count, all
                           of the words you have on the board
                           after placing the letters\n
                           need to be found in a dictionary
                           and every word needs
                           to be glued to another (they need to shere\n
                           at least one letter).\n\n
                           1. Starting the game\n
                           On your left side
                           there is a board (size: 15X15),where
                           you need to place your letters.\n
                           On your right you can see
                           a label informing about which
                           player's turn it is and his score.\n
                           Your tiles are displayed below
                           and on the left you will
                           see a functional buttons.\n
                           On the right side there is
                           an information about points
                           you get using a particular letter\n\n
                           When you are the one making the first move you must
                           start placing your word
                           on the special square with # on.\n
                           After each correct move your rack is being filled
                           and your score increased.\n
                           In case of incorrect move you will be notified
                           and you will loose your turn.\n\n
                           2. Functional buttons:\n
                           SKIP - loose your turn with no move\n
                           HINT - program will provide you a word
                           and place it on a board\n
                           EXCHANGE ALL - exchange all your letters\n
                           EXCHANGE ONE - exchange one letter, choose it by
                           clicking on the tile\n
                           UNDO MOVE - undo your entire move and
                           start placing the letters again
                           END MOVE - confirm your move (it will be checked)\n
                           \n
                           3. End of the game\n
                           The game is over if one of the player reach
                           50 points or there are no more letters in the Bag.\n
                           The winner's name is displayed on the screen.
                           """

    def viewInstruct(self):
        """
            This function returns instruction
            :return: string - instruction

        """

        return self.instruction
