from ui_manager import UIManager
from map_manager import MapManager
from file_manager import FileManager

from instances.item import Item
from instances.enemy import Enemy
from instances.player import Player


class GameManager:
    def __init__(self):
        self.ui_manager = UIManager()
        self.event_manager = MapManager()
        self.file_manager = FileManager()

        self.player = Player()
        self.item = Item()
        self.enemy = Enemy()



