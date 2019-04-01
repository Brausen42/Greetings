from Tokenizable import Tokenizable

class Company(Tokenizable):
    def __init__(self, obj = None):
        self.id = None #Number
        self.company = None #string
        self.city = None #string
        self.timezone = None #string
        if obj:
            self.id = obj["id"] if "id" in obj else None
            self.company = obj["company"] if "company" in obj else None
            self.city = obj["city"] if "city" in obj else None
            self.timezone = obj["timezone"] if "timezone" in obj else None

    def getTokens(self):
        tokens = {}
        tokens["COMPANY.COMPANY"] = lambda tokens : str(self.company)
        tokens["COMPANY.CITY"] = lambda tokens : str(self.city)
        tokens["TIMEZONE"] = lambda tokens : str(self.timezone) # special shared variable so we use 'TIMEZONE'
        return tokens