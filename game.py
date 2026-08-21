class Game:
    def __init__(self,name):
        self.player = None
        self.name = name

    def add_player(self, player):
        self.player = player

    def introduction(self):
        """ NSEW , UD """
        import time
        print(f" Hello {self.name} Welcome to 5 nights at EPSTEIN's")
        print(f" In this game you will have 5 rounds to escape EPSTEIN , with each round getting harder and harder")
        time.sleep(2)

        print("You will be using NSEW for navigation and U for Up")
        time.sleep(1)
        print("The game will be starting shortly")

    
    def attack(self):
        pass

    def get_options(self):
        pass

    def get_actions(self, choice):
        pass

    def game_over(self):
        pass

    def epilogue(self):
        """ display game over"""
        import time
        print(f" Awwww GAME OVER , better luck next time")
        time.sleep(2)
        print(f"better luck next time")
