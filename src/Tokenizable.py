class Tokenizable:
    """Abstract class to inherit when a class is going to be used in MessageTemplates"""

    def __init_(self):
        pass

    @staticmethod
    def wrapValue(value):
        """utility method for wrapping a value in a way that can be used as a token expression"""
        return (lambda tokens: str(value))

    def getTokens(self):
        raise NotImplementedError