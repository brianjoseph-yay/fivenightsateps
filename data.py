class Player:
    def __init__(self):
        self.hp = 20 # pre-set health level
        self.attack = 2 # bare-handed punch
        self.money = 0
        self.inventory = []
        self.map = stack()
        
    def get_hp(self):
        return self.hp

    def update_status(self):
        if self.hp <= 0:
            self.status = "dead"

    def lose_hp(self, value):
        if not isinstance(item, (str, float)):
            raise ValueError

        self.hp -= value
        self.update_status

    def gain_hp(self, value):
        if not isinstance(item, (str, float)):
            raise ValueError

        self.hp += value

    def update_attack(self, update):
        if not isinstance(update, (str, float)):
            raise ValueError
        self.attack += update
        

    def get_inventory(self):
        return self.inventory

    def insert_inventory(self,item):
        """ once purchased item from shop , place into inventory (max 5 items) """
        
        if len(self.inventory) == 5:
            return "Inventory full!"
        
        self.inventory.append(item)
    """
    def get_money(self):
        return self.money

    def set_money(self,item):
        if not isinstance(item, (str, float)):
            raise ValueError
        
        self.money += item
    """

class Item:
    def __init__(self, name, func, count):
        self.name = name
        self.func = funcs
        self.count = count

    def get_count(self):
        return self.count

    def get_name(self):
        return self.name

    def update_count(self):
        if count <= 0:
            return False #no more use left
        
        self.count -= 1
    
    def get_func(self):
        self.update_count()

        return self.func


class Monster(Player):
    def __init__(self, hp, attack, description):
        self.hp = hp
        self.atk = attack
        self.des = description
        self.status = "alive"

    def get_hp(self):
        return self.hp
    
    def get_attack(self):
        return self.atk

    def get_description(self):
        return self.des

class Room:
    def __init__(self, contents, exits):
        self.contents = contents
        self.exits = exits #dict
        self.next = {"north" : None, "east" : None, "south" : None, "west" : None}
    
    def get_exits(self):
        return self.exits
    
    def get_contents(self):
        return self.contents


class stack: #mapping of the rooms on a level
    def __init__(self):
        self.head = None
        self.pointer = None
        self.retreat_direction = None

    def push(self, room, direction):
        if direction == "north":
            self.retreat_direction = "north"
        elif direction == "south":
            self.retreat_direction = "south"
        elif direction == "east":
            self.retreat_direction = "east"
        elif direction == "west":
            self.retreat_direction = "west"

        if self.head is None:
            self.head = room
            self.pointer = room
            return

        current = self.pointer
        self.pointer.next[direction] = room
        self.pointer.next[self.retreat_direction] = current
        self.pointer = room

    def forward(self, direction):
        current = self.pointer
        if current.next[direction] is not None:
            self.pointer = current.next[direction]

            if direction == "north":
                self.retreat_direction = "south"
            elif direction == "south":
                self.retreat_direction = "north"
            elif direction == "east":
                self.retreat_direction = "west"
            elif direction == "west":
                self.retreat_direction = "east"

            return
        return "dead end"

    def retreat(self):
        if self.retreat_direction is None:
            return "you are at the start"
        return self.pointer.next[self.retreat_direction]

test = stack()
test.push(Room(1, {"north" : None, "east" : None, "south" : None, "west" : None}), "south")
print(test.pointer)
test.push(Room(2, {"north" : None, "east" : None, "south" : None, "west" : None}), "north")
print(test.pointer)