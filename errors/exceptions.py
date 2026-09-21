class AcademyError(Exception):
    pass

class InvalidAttributeError(AcademyError):
    pass

class RegistrationError(AcademyError):
    pass

class AcademyDBError(AcademyError):
    pass

class PlayerDoesNotExistError(AcademyError):
    pass

class EmptyAcademyError(AcademyError):
    pass