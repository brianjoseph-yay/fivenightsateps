import random

import data


class Game:
    def __init__(self,name):
        self.player = None
        self.name = name
        self.movement = []
        self.is_gameover = False
        

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

    
    def attack(self, monster: data.monster,is_attacking : bool, item: data.Item):
        player = self.player
        if is_attacking == "P":
            damage = player.attack # bare-handed attack by player
            if item:
                if item.name== "taser":
                    if item.usecount > 0:
                        monster.take_damage(item.damage) 

                elif item.name == "oil":
                     if item.usercount > 0:
                          player.gain_hp(item.regeneration)
                     
                        
            else:
                """ attacking monster bare-handed"""
                monster.hp -= damage
        if is_attacking == "M":
            # damage done by monster is randomised
            damage = random.randint(2,4)
            player.hp -= damage


    def get_options(self,is_attacking,room:data.room):
        """ shows the options , Attack , healing etc"""
        if is_attacking:
            return ["Attack","Access Inventory","Retreat"]
        else:
            bin_list = []
            for exits in room.getExits():
                bin_list.append(exits)
            result = bin_list + ["Attack","Access Inventory","Retreat"]
            return result


    def get_actions(self, choice):
        player = self.player
        if choice == "Attack":
            return self.attack()
        elif choice == "Inventory":
            return player.get_inventory()
        elif choice == "Retreat":
            return player.map.retreat()
        elif choice == "N":
            return player.map.forward("north")
        elif choice == "S":
                    return player.map.forward("south")
        elif choice == "E":
                    return player.map.forward("east")
        else:
            return player.map.forward("west")
        

    def epilogue(self):
        """ display game over"""
        import time
        print(f" Awwww GAME OVER , better luck next time")
        time.sleep(2)
        print(f"better luck next time")


    


        



    
