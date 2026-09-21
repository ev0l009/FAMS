from helpers.validators import require_non_empty_str
from helpers.validators import validate_age
from helpers.validators import validate_rating

class Player:
    def __init__(self, name: str, age: int, position: str, rating: int | float) -> None:
        require_non_empty_str(name, "Player name")
        validate_age(age)
        require_non_empty_str(position, "Player position")
        validate_rating(rating)

        self.name = name
        self.age = age
        self.position = position
        self.rating = float(rating)

    def __str__(self) -> str:
        return (
            "=====================\n"
            "      PLAYER INFO\n"
            "=====================\n"
            f"Name:       {self.name}\n"
            f"Age:        {self.age}\n"
            f"Position:   {self.position}\n"
            f"Rating:     {self.rating}\n"
        )