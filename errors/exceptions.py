"""Contains all academy custom exceptions"""

class AcademyError(Exception):
    """Generic academy exception"""
    pass

class InvalidAttributeError(AcademyError):
    """Sub-academy exception for invalid academy and player attributes related errors"""
    pass

class RegistrationError(AcademyError):
    """Sub-academy exception for registration errors"""
    pass

class AcademyDBError(AcademyError):
    """Sub-academy exception for errors related to academy database"""
    pass

class PlayerDoesNotExistError(AcademyError):
    """Sub-academy exception for search related errors"""
    pass

class EmptyAcademyError(AcademyError):
    """Sub-academy exception triggered when the academy has no registered players"""
    pass