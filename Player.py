import keyboard
import time
from Ship import Ship

class Player(object):
    
    # à mettre dans un json
    SHIPS = [
        {
            "name" : "Porte-avion",
            "length" : 5,
            "position" : [],
            "count": 1
        },
        {
            "name" : "Croiseur",
            "length" : 4,
            "position" : [],
            "count" : 1
        },
        {
            "name" : "Contre-torpilleur",
            "length" : 3,
            "position" : [],
            "count" : 2
        },
        {
            "name" : "Torpilleur",
            "length" : 2,
            "position" : [],
            "count" : 1
        }
    ]

    def __init__(self, name):
        self.name = name
        self.fleet = self.generate_fleet()
        self.shoots = []
    
    # generates ships for a player
    def generate_fleet(self):
        ships = []
        for s in self.SHIPS:
            for i in range(s["count"]):
                ships.append(Ship(s["name"], s["length"]))
        return ships

    def place(self):
        pos = {
            "y-axis" : 0,
            "x-axis" : 9,
            "vertical" : True            
        }
        for ship in self.fleet:
            board = ship.update(pos)
            board.print()
            while not ship.position: 
                print("Placement de votre", ship.name, "...")
                board.cells[pos["x-axis"]][pos["y-axis"]] = " ☐ "
                if ["y-axis"] == len(board.cells) - 1:
                    board.cells[pos["x-axis"]][pos["y-axis"]] += "\n"
                if keyboard.is_pressed('up arrow'): 
                    pos["x-axis"] -= 1
                if keyboard.is_pressed('down arrow'): 
                    pos["x-axis"] += 1
                if keyboard.is_pressed('left arrow'): 
                    pos["y-axis"] -= 1
                if keyboard.is_pressed('right arrow'): 
                    pos["y-axis"] += 1
                if keyboard.is_pressed('r'): 
                    pos["vertical"] = not pos["vertical"]
                board = ship.update(pos)
                board.print()
                time.sleep(.1)
