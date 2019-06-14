class CustomExceptions(Exception):
    """Base class for custom exceptions"""
    pass

class WrongAnswerToYesNoQuestion(CustomExceptions):
    """Raised when input from Yes/No question is not 'yes', 'no'"""
    pass

class ValueNotBetweenThreeAndSix(CustomExceptions):
    """Raised when input is not between 3 and 6"""
    pass