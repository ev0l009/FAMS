"""Contains all academy custom exceptions"""

class AcademyError(Exception):
    """Generic academy error"""
    pass

class InvalidAttributeError(AcademyError):
    """Sub-academy error for invalid academy and player attributes"""
    pass

class RegistrationError(AcademyError):
    """Sub-academy error for registration exceptions"""
    pass

class AcademyDBError(AcademyError):
    """Sub-academy error for issues related to academy database"""
    pass

class PlayerDoesNotExistError(AcademyError):
    """Sub-academy error for searching missing or unregistered players"""
    pass

class EmptyAcademyError(AcademyError):
    """Sub-academy error triggered when the academy has no registered players"""
    pass