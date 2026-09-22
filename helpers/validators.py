"""Contains helpful validators to check values before an academy or player methods are executed."""

# required to raise exceptions (see exceptions in error module)
from errors.exceptions import InvalidAttributeError
from errors.exceptions import EmptyAcademyError

# global rating config for players
MIN_RATING = 0.0
MAX_RATING = 10.0

def require_non_empty_str(value: str, field: str):
    """Checks whether a string value is not empty.
    
    Args:
        value (str): expected value to be checked.
        field (str): field name to raise error.
        
    Returns: 
        None
    
    Raises:
        InvalidAttributeError: field name and value must be strings.
        InvalidAttributeError: value must be a non-empty string.
    """
    if type(value) is not str or type(field) is not str:
        raise InvalidAttributeError(f"Value and Field must be strings.")
    if not value.strip() :
        raise InvalidAttributeError(f"Err: {field} cannot be empty.")

def validate_age(value: str | int):
    """Checks whether age  is valid. 

    Args:
        value (str | int): player's age.
    
    Returns: 
        None

    Raises:
        InvalidAttributeError: age must be an integer.
        InvalidAttributeError: age must be greater than or equal to 15.
    """
    try:
        value = int(value)
    except ValueError:
        raise InvalidAttributeError("Err: Age must be an integer.")
    if value < 15:
        raise InvalidAttributeError("Err: Age cannot be less than 15.")

def validate_rating(value: str |int | float):
    """Checks whether rating value is valid

    Args:
        value (str |int | float): player's rating

    Returns:
        None
    
    Raises:
        InvalidAttributeError: rating must be an integer or a float
        InvalidAttributeError: rating is out of min-max range
    """
    try:
        value = float(value)
    except ValueError:
        raise InvalidAttributeError("Err: Rating must be an integer or a float")
    if value < MIN_RATING or value > MAX_RATING:
        raise InvalidAttributeError(f"Err: Rating out of range of {MIN_RATING}-{MAX_RATING}")

def require_non_empty_academy(value:  int) -> None:
    """Checks whether academy is empty

    Args:
        value (int): current length of registered players in the academy

    Returns:
        None
    
    Raises:
        EmptyAcademyError: Academy should have at least one player for required task to execute.
    """
    if value < 1:
        raise EmptyAcademyError("Operation requires at least one player")