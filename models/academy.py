from helpers.validators import require_non_empty_str

from errors.exceptions import RegistrationError

from typing import Self

# from typing import TypedDict

# class PlayerType(TypedDict):
#     name: str
#     age: int
#     position: str
#     rating: int | float

from models.player import Player

DB_PATH = "./db/players.txt"

class Academy:
    def __init__(self, name: str) -> None:
        require_non_empty_str(name, "Academy name")
        self.name = name
        self.players: dict[str, "Player"] = {}

    def __len__(self) -> int:
        return len(self.players)

    def __str__(self) -> str:
        return (
            "=====================\n"
            f"      {self.name.title()}\n"
            "=====================\n"
            f"Registered Players: {len(self.players)}"
        )

    def add_player(self, player: "Player") -> Self:
        if player.name.lower() in self.players:
            raise RegistrationError("Player with same name is already registered")
        self.players[player.name.lower()] = player
        return self

    def update_academy_players(self) -> Self:
        with open(DB_PATH, "w") as file:
            for key, player in self.players.items():
                file.write(
                    f"'{key}' : {{\n"
                    f"\t'name': '{player.name}',\n"
                    f"\t'age': {player.age},\n"
                    f"\t'position': '{player.position}',\n"
                    f"\t'rating': {player.rating},\n"
                    "},\n"
                )
        return self

    def load_academy_players(self) -> Self:
        # player_list = []
        with open(DB_PATH, "r") as file:
            for line in file:

        return self