import re
from datetime import datetime
from Tokenizable import Tokenizable
from Timezone import Timezone

class UndefinedToken(Exception):
    pass

def _timebasedGreeting(tokens):
    timezone = Timezone(tokens["TIMEZONE"](tokens))
    timeOfDay = timezone.getTimeOfDay(datetime.now())
    return "Good " + timeOfDay

class MessageTemplate():
    def __init__(self, obj):
        self.id = None #string - default to 'None' until we have a way to generate a unique ID
        self.tokens = {} #dict - active tokens for use in message. Priority over the defaults.
        self.defaultTokens = {} #dict - defaults to fill in tokens that no Tokenizable object populates
        self._builtins = {
            "GREETING": _timebasedGreeting
        }
        self.message = "" #string

        self._pattern = re.compile('[$][{](\S+)[}]') # find tokens that look like '${...}'
        self.clearDefaults() # populate 'defaultTokens'

        if obj:
            self.id = str(obj["id"]) if "id" in obj else None
            if "defaults" in obj:
                self.setDefaults(dict(obj["defaults"]))
            self.message = obj["message"] if "message" in obj else None

    def clearDefaults(self):
        self.defaultTokens.clear()
        self.defaultTokens.update(self._builtins)
    
    def setDefaults(self, defaults):
        for key in defaults:
            self.defaultTokens[key] = Tokenizable.wrapValue(defaults[key])

    def clearValues(self):
        self.tokens.clear()

    def loadValues(self, tokenizableObj):
        self.tokens.update(tokenizableObj.getTokens())

    def createMessage(self):
        currentTokens = self.defaultTokens.copy()
        currentTokens.update(self.tokens)
        message = self.message

        tokens = self._pattern.findall(message)
        depth = 0
        while len(tokens) > 0:
            for token in tokens:
                if token in currentTokens:
                    message = message.replace("${" + token + "}", currentTokens[token](currentTokens))
                else:
                    raise UndefinedToken
            tokens = self._pattern.findall(message)
            depth = depth + 1
            if depth > 100:
                raise Exception("Token depth limit exceeded")

        return message
