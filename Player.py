class Player:
    """ An class representing a Player.

        Attributes:
            score: An integer representing the Player's current score.
            blocks_taken: A list of Blocks which belong to the Player.
    """

    def __init__(self):
        """ Initializes a Player.
        """

        # Initializes member variables.
        self.score = 0
        self.bonuses_taken_per_color = {}

    def set_colors(self, colors):
        """ Initializes player colors, depending on the num_colors setting of the game.

            This function should be called in Game.py during Game initialization.

            Args:
                colors: A list of colors generated by Game.
        """

        for color in colors:
            self.bonuses_taken_per_color[color] = 0

    def evaluate_moves(self, legal_moves):
        """ Evaluates and selects an optimum move.

            Args:
                legal_moves: A list of legal moves.

            Returns:
            i: An integer representing the x position of the chosen move.
            j: An integer representing the y position of the chosen move.
        """

        # Return dummy values
        return 0, 0

    def score_block(self, block):
        """ Adds block value to player score; if it is worth 1, increments color dict.

            Args:
                block: The block that the player took during their turn.
        """

        self.score += block.value

        if block.value == 1:
            self.bonuses_taken_per_color[block.color] += 1

    def pretty_print(self):
        """ Pretty-prints player's score and colors.
        """

        print("    Score: " + str(self.score))
        print("    Colors: " + str(self.bonuses_taken_per_color))
