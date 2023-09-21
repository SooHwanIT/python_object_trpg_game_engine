class Player:
    def __init__(self):
        self.level = 0

        self.hp = 0
        self.mp = 0

        self.max_hp = 0
        self.max_mp = 0

        self.stk = 0
        self.vit = 0
        

    def get_player_hp(self):
        return self.hp

    def get_player_mp(self):
        return self.mp

    def set_player_hp(self, hp):
        self.hp = hp

    def set_player_mp(self, mp):
        self.mp = mp

