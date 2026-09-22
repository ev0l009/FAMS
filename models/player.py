"""Contains the player class and methods"""

# required to validate values before executing player methods
from helpers.validators import require_non_empty_str
from helpers.validators import validate_age
from helpers.validators import validate_rating

class Player:
    """
    Initializes a player and contains player methods.

    Attributes:
        name (str): player's name
        age (int): player's age
        position (str): player's position
        rating (int | float): player's rating
    """
    def __init__(self, name: str, age: int, position: str, rating: int | float) -> None:
        """
        Initializes a player instance

        Args:
            name (str): player's name
            age (int): player's age
            position (str): player's position
            rating (int | float): player's rating

        Example:
            >>> player = Player("Val", 34, "CF", 7.8)
        
        Raises:
            InvalidAttributeError: Player's name must be a non-empty string
            InvalidAttributeError: Player's age must be an integer greater than or equal to 15
            InvalidAttributeError: Player's position must be a non-empty string
            InvalidAttributeError: Player's rating must be an integer or float with min-max range (see validators module)
        """
        require_non_empty_str(name, "Player name")
        validate_age(age)
        require_non_empty_str(position, "Player position")
        validate_rating(rating)

        self.name = name
        self.age = age
        self.position = position
        self.rating = float(rating)

    def __str__(self) -> str:
        """
        Returns basic player info in easy-to-read format.

        Example:
            >>> print(Player("Val", 24, "CDM", 8.3))

        Returns:
            Basic info about a player as strings
        """
        return (
            "=====================\n"
            "      PLAYER INFO\n"
            "=====================\n"
            f"Name:       {self.name}\n"
            f"Age:        {self.age}\n"
            f"Position:   {self.position}\n"
            f"Rating:     {self.rating}\n"
        )