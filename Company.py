from Tokenizable import Tokenizable

class Company(Tokenizable):
    def __init__(self, obj = None):
        self.id = None #string - default to 'None' until we have a way to generate a unique ID
        self.company = "" #string
        self.city = "" #string
        self.timezone = "" #string
        if obj:
            self.id = str(obj["id"]) if "id" in obj else None
            self.company = obj["company"] if "company" in obj else ""
            self.city = obj["city"] if "city" in obj else ""
            self.timezone = obj["timezone"] if "timezone" in obj else ""

    def getTokens(self):
        tokens = {}
        tokens["COMPANY.COMPANY"] = Tokenizable.wrapValue(self.company)
        tokens["COMPANY.CITY"] = Tokenizable.wrapValue(self.city)
        tokens["TIMEZONE"] = Tokenizable.wrapValue(self.timezone) # special shared variable so we use 'TIMEZONE'
        return tokens