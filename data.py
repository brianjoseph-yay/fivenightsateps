import random

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

    def prompt_player_choice(self):
        return input("> ")

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
    def __init__(self, contents, exits, is_final : bool):
        self.contents = contents
        self.exits = exits #dict
        self.next = {"north" : None, "east" : None, "south" : None, "west" : None}
        self.is_final = is_final

    def __repr__(self):
        return str(self.contents)
    
    def get_exits(self):
        return self.exits
    
    def get_contents(self):
        return self.contents

    def is_final(self):
        return self.is_final


class stack: #mapping of the rooms on a level
    def __init__(self):
        self.head = None
        self.pointer = None
        self.retreat_path = []

    def push(self, room, direction):
        if room.is_final:
            return "final" # reached final room

        if direction == "north":
            self.retreat_path.append("south")
        elif direction == "south":
            self.retreat_path.append("north")
        elif direction == "east":
            self.retreat_path.append("west")
        elif direction == "west":
            self.retreat_path.append("east")

        if self.head is None:
            self.head = room
            self.pointer = room
            return False

        current = self.pointer
        self.pointer.next[direction] = room
        self.pointer = room
        self.pointer.next[self.retreat_path[-1]] = current
        return False

    def forward(self, direction):
        current = self.pointer
        if current.next[direction] is not None:
            self.pointer = current.next[direction]

            if direction == "north":
                self.retreat_path.append("south")
            elif direction == "south":
                self.retreat_path.append("north")
            elif direction == "east":
                self.retreat_path.append("west")
            elif direction == "west":
                self.retreat_path.append("east")

            if self.pointer.is_final:
                return "final" # reached final room

            return False
        return "dead end"

    def retreat(self):
        if self.retreat_path is None or self.pointer is None:
            return "you are at the start"

        if self.pointer.is_final:
            return "final" # reached final room

        retreat_direction = self.retreat_path.pop(-1)
        self.pointer = self.pointer.next[retreat_direction]

        direction = retreat_direction
        if direction == "north":
            self.retreat_path.append("south")
        elif direction == "south":
            self.retreat_path.append("north")
        elif direction == "east":
            self.retreat_path.append("west")
        elif direction == "west":
            self.retreat_path.append("east")
        
        return False

    def display_visual_map(self):
        visual_map = ""
        for _ in range(10):
            for _ in range(10):
                visual_map += ""

test = stack()
test.push(Room(1, {"north" : None, "east" : None, "south" : None, "west" : None}, False), "south")
print(test.pointer.contents, test.retreat_path)
test.push(Room(2, {"north" : None, "east" : None, "south" : None, "west" : None}, False), "east")
print(test.pointer.contents, test.retreat_path)
test.retreat()
print(test.pointer.contents, test.retreat_path)
test.forward("east")
print(test.pointer.contents, test.retreat_path)
test.push(Room(3, {"north" : None, "east" : None, "south" : None, "west" : None}, False), "north")
test.push(Room(4, {"north" : None, "east" : None, "south" : None, "west" : None}, False), "north")
test.push(Room(5, {"north" : None, "east" : None, "south" : None, "west" : None}, False), "west")
test.push(Room(6, {"north" : None, "east" : None, "south" : None, "west" : None}, False), "west")
print(test.pointer.contents, test.retreat_path)


#implementation for the map

all_rooms, searched = [], set()
current = test.head
all_rooms.append(current)
searched.add(current)
def mapping(current):
    global all_rooms, mapping, searched
    for direction, room in current.next.items():
        if room is None:
            continue
        if room in searched:
            continue

        all_rooms.append(room)
        searched.add(room)
        mapping(room)

mapping(current)
print(all_rooms)


def random_gen(mapping, item):
    idx = random.randint(0, len(mapping)-1)
    mapping[idx].contents.append(item)


#implmentation for multi-layered mapping

class Layer:
    def __init__(self):
        self.levels = []
        self.pointer = None

    def add_level(self, Map, level : (int, bool)):
        if not self.levels:
            self.levels.append(Map)
            self.pointer = 0
            return

        if level is None:
            self.levels.append(Map)
            return
        
        self.levels.insert(level, Map)
        if level <= self.pointer and level > 0:
            self.pointer += 1

    def move_up(self):
        self.pointer += 1
        if self.pointer >= len(self.levels):
            raise IndexError("max_storey reached")

        return self.levels[pointer]

    def move_down(self):
        self.pointer += 1
        if self.pointer < 0:
            raise IndexError("min_storey reached")

        return self.levels[pointer]
