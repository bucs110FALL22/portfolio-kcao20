class Player:
    def __init__(self, pnum):
        """
        Initialize the player object
        args: pnum [int] the player's id
        """
        self.player_num = pnum
        self.lives = 3  # how many tries a player has
        self.hp = 1  # how much damage the character can take before dying
        self.form = 0  # mario is at small base form by default


class Block:
    def __init__(self, tnum=0):
        """
        Initialize block objects that could be a brick or mystery box
        args: tnum [int] the type of block (brick by default)
        """
        self.type = tnum  # changes the blocks properties / sprites
        self.hp = 1  # how much damage the block can take before breaking
        self.activated = 0  # determines if an object is released


class Goomba:
    def __init__(self):
        """
        Initialize Goombas
        """
        self.color = 0  # changing color for goomba
        self.alive = 0  # determines if goomba is alive or not
        self.direction = 0  # goomba moving left or right
