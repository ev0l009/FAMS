from helpers.validators import require_non_empty_str

from errors.exceptions import RegistrationError
from errors.exceptions import AcademyDBError
from errors.exceptions import PlayerDoesNotExistError

from typing import Self

import json
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
            raw_data = {
                key: player.__dict__
                for key, player in self.players.items()
            }
            json.dump(raw_data, file, indent=4)
        return self

    def load_academy_players(self) -> Self:
        try:
            with open(DB_PATH, "r") as file:
                raw_data = json.load(file)
                self.players = {
                    key: Player(**player_dict) 
                    for key, player_dict in raw_data.items()
                }
        except (FileNotFoundError, json.JSONDecodeError):
            raise AcademyDBError("Err: Couldn't load academy players data.")
        return self

    def find_player(self, name: str) -> "Player":
        require_non_empty_str(name, "Player name")
        if name.lower() in self.players:
            return self.players[name.lower()]
        raise PlayerDoesNotExistError(f"Err: {name} is not a registered player.")

    def remove_player(self, name: str) -> Self:
        require_non_empty_str(name, "Player name")
        self.players.pop(self.find_player(name).name.lower())
        return self