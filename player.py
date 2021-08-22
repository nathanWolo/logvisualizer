class Player:
    def __init__(self, steam_id) -> None:
        self.steam_id = steam_id
        self.games = 0
    def add_game(self):
        self.games += 1
    def get_id(self) -> str:
        return self.steam_id