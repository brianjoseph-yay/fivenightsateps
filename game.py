class Game:
    def __init__(self,name):
        self.name = name

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

    def win(self):
        pass

    def lose(self):
        pass


class Player:
    def __init__(self):
        self.hp= 20 # pre-set health level
        self.attack = 2 # bare-handed punch
        self.money = 0
        
    def get_hp(self):
        pass


    def attack(self):
        pass

    def get_inventory(self):
        pass

    def insert_inventory(self,item):
        """ once purchased item from shop , place into inventory (max 5 items) """
        pass

    def navigation(self,direction):
        pass


    def get_money(self):
        pass

    def set_money(self,item):
        pass



    


        



    
