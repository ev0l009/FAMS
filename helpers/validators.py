from errors.exceptions import InvalidAttributeError
from errors.exceptions import EmptyAcademyError

MIN_RATING = 0.0
MAX_RATING = 10.0

def require_non_empty_str(value: str, field: str):
    if type(value) is not str or type(field) is not str:
        raise InvalidAttributeError(f"Value and Field must be a non-empty string.")
    if not value.strip():
        raise InvalidAttributeError(f"Err: {field} cannot be empty.")

def validate_age(value: int):
    if type(value) is not int:
        raise InvalidAttributeError("Err: Age must be an integer.")
    if value < 15:
        raise InvalidAttributeError("Err: Age cannot be less than 15.")

def validate_rating(value: int | float):
    if type(value) is not int and type(value) is not float:
        raise InvalidAttributeError("Err: Rating must be an integer or a float")
    if value < MIN_RATING or value > MAX_RATING:
        raise InvalidAttributeError(f"Err: Rating out of range of {MIN_RATING}-{MAX_RATING}")

def require_non_empty_academy(value:  int) -> None:
    if value < 1:
        raise EmptyAcademyError("Operation requires at least one player")