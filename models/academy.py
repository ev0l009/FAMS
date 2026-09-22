"""Contains the academy class and its methods"""

# required to validate values before academy methods can execute
from helpers.validators import require_non_empty_str
from helpers.validators import require_non_empty_academy

# required to raise relevant exceptions
from errors.exceptions import RegistrationError
from errors.exceptions import AcademyDBError
from errors.exceptions import PlayerDoesNotExistError

# required for type hinting
from typing import Self
from models.player import Player

# required to write to and load from academy database
import json

# global academy database file path 
DB_PATH = "./db/players.json"

class Academy:
    """
    Creates an academy instance and contains academy methods.
    
    Attributes:
        name (str): official name of the academy
    """

    def __init__(self, name: str) -> None:
        """
        Creates an academy instance. Necessary to run any other academy method

        Attributes:
            name (str): official name of the academy
        
        Example:
            >>> academy = Academy("My academy")

        Returns:
            None

        Raises:
            InvalidAttributeError: Academy name must be a non-empty string
        """
        require_non_empty_str(name, "Academy name")
        self.name = name
        self.players: dict[str, "Player"] = {}

    def __len__(self) -> int:
        """
        Returns the number of registred players in the academy.

        Example:
            >>> print(len(academy))

        Returns:
            The count of registered players as an integer.
        """
        return len(self.players)

    def __str__(self) -> str:
        """
        Returns basic info about the academy in easy-to-read format

        Example:
            >>> print(academy)

        Returns:
            Basic easy-to-read info about the academy as strings 
        """
        return (
            "=====================\n"
            f"      {self.name.title()}\n"
            "=====================\n"
            f"Registered Players: {len(self.players)}"
        )

    def add_player(self, player: "Player") -> Self:
        """
        Adds a player to the academy

        Args:
            player (Player): player object (see player module in models)
        
        Example:
            >>> academy.add_player(Player("Val", 24, "CDM", 7.8))
        
        Returns:
            Academy instance for method chaining.

        Raises:
            RegistrationError: Cannot add an already registered player.
        """
        if player.name.lower() in self.players:
            raise RegistrationError("Player with same name is already registered")
        self.players[player.name.lower()] = player
        return self

    def update_academy_players(self) -> Self:
        """
        Stores player data in database.

        Example:
            >>> academy.update_academy_players()

        Returns:
            Academy instance for method chaining.

        Raises:
            AcademyDBError: Database file doesn't exist
        """
        try:
            with open(DB_PATH, "w") as file:
                raw_data = {
                    key: player.__dict__
                    for key, player in self.players.items()
                }
                json.dump(raw_data, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            raise AcademyDBError("Err: Couldn't save academy players data.")
        return self

    def save_academy_players(self) -> Self:
        """
        Loads player data from database.

        Example:
            >>> academy.save_academy_players()

        Returns:
            Academy instance for method chaining.

        Raises:
            AcademyDBError: Database file doesn't exist
        """
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
        """
        Searches for a player by name.

        Args:
            name (str): player name

        Example:
            >>> academy.find_player("Val")
        
        Returns:
            A player object

        Raises:
            InvalidAttributeError - Player name must be a non-empty string
            PlayerDoesNotExistError: Player does not exist in academy records.
        """
        require_non_empty_str(name, "Player name")
        if name.lower() in self.players:
            return self.players[name.lower()]
        raise PlayerDoesNotExistError(f"Err: {name} is not a registered player.")

    def remove_player(self, name: str) -> Self:
        """
        Removes a player from the academy.

        Args:
            name (str): name of player to be removed

        Example:
            >>> academy.remove_player("Val")

        Returns:
            Academy instance for method chaining.

        Raises:
            InvalidAttributeError: Player name must be a non-empty string
            PlayerDoesNotExistError: Player does not exist in academy records.
        """
        require_non_empty_str(name, "Player name")
        self.players.pop(self.find_player(name).name.lower())
        return self

    def average_rating(self) -> float:
        """
        Returns the average rating of all registered players.

        Examples:
            >>> academy.average_rating()
        
        Returns:
            Average rating of all players in the academy as float

        Raises:
            EmptyAcademyError: Academy needs to have at least one player.
        """
        require_non_empty_academy(len(self.players))
        total_rating: float = 0.0
        for player in self.players:
            total_rating += self.players[player].rating
        return total_rating/len(self.players)

    def top_player(self) -> "Player":
        """
        Returns the player with the highest rating.

        Examples:
            >>> academy.top_player()
        
        Returns:
            Player with the highest rating in the academy as object

        Raises:
            EmptyAcademyError: Academy needs to have at least one player.
        """
        require_non_empty_academy(len(self.players))
        players: list[Player] = list(self.players.values())
        current_top_player = players[0]
        for player in players:
            if player.rating > current_top_player.rating:
                current_top_player.rating = player.rating
        return current_top_player