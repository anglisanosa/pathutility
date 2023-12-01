


class InvalidPropertyError(Exception):
    """Raised when an invalid property is provided"""
    def __init__(self, message="Invalid property provided. Allowed properties:"):
        self.message = message
        super().__init__(self.message)

class FileOperationError(Exception):
    """Raised for file operation related errors"""
    pass