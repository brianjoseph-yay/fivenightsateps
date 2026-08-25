"""main.py

The main game loop.
"""
# By convention, import statements go at the top of the file

import game
import data

""" in data.py pls create a function called create player takes in no arguemnts that returns player object"""
if __name__ == "__main__":
    gameObj = game.Game()
    gameObj.introduction()
    player = data.create_player()
    gameObj.add_player(player)



    while not gameObj.is_gameover:
        choices = gameObj.get_options()
        choice = data.prompt_player_choice(choices)
        gameObj.execute(choice)
        data.display(gameObj.status())
    game.epilogue()
    
