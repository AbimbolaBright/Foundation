from random import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()



# SPRITE_SCALING_COIN = 0.2

# coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)



# def setup(self):
#     """ Set up the game and initialize the variables. """

#     # Create the sprite lists
#     self.player_list = arcade.SpriteList()
#     self.coin_list = arcade.SpriteList()

#     # Score
#     self.score = 0

#     # Set up the player
#     # Character image from kenney.nl
#     self.player_sprite = arcade.Sprite("images/character.png")
#     self.player_sprite.center_x = 50 # Starting position
#     self.player_sprite.center_y = 50
#     self.player_list.append(self.player_sprite)

#     # Create the coins
#     for i in range(COIN_COUNT):

#         # Create the coin instance
#         # Coin image from kenney.nl
#         coin = arcade.Sprite("images/coin_01.p)

#         # Position the coin
#         coin.center_x = random.randrange(SCREEN_WIDTH)
#         coin.center_y = random.randrange(SCREEN_HEIGHT)

#         # Add the coin to the lists
#         self.coin_list.append(coin)





MOVEMENT_SPEED = 5

def on_key_press(self, key, modifiers):
    """Called whenever a key is pressed. """

    if key == arcade.key.UP:
        self.player_sprite.change_y = MOVEMENT_SPEED
    elif key == arcade.key.DOWN:
        self.player_sprite.change_y = -MOVEMENT_SPEED
    elif key == arcade.key.LEFT:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = MOVEMENT_SPEED

def on_key_release(self, key, modifiers):
    """Called when the user releases a key. """

    if key == arcade.key.UP or key == arcade.key.DOWN:
        self.player_sprite.change_y = 0
    elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
        self.player_sprite.change_x = 0



def update(self, delta_time):
    """ Movement and game logic """

