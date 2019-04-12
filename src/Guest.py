from Tokenizable import Tokenizable
from Reservation import Reservation

class Guest(Tokenizable):
    """Class that represents a Guest at a hotel, or some other kind of reservable location"""

    def __init__(self, obj = None):
        self.id = None #string - default to 'None' until we have a way to generate a unique ID
        self.firstName = "" #string
        self.lastName = "" #string
        self.reservation = Reservation() #Reservation
        if obj:
            self.id = str(obj["id"]) if "id" in obj else None
            self.firstName = obj["firstName"] if "firstName" in obj else ""
            self.lastName = obj["lastName"] if "lastName" in obj else ""
            if "reservation" in obj:
                self.reservation = Reservation(obj["reservation"])

    def getTokens(self):
        tokens = {}
        tokens["GUEST.FIRSTNAME"] = Tokenizable.wrapValue(self.firstName)
        tokens["GUEST.LASTNAME"] = Tokenizable.wrapValue(self.lastName)
        tokens["GUEST.FULLNAME"] = Tokenizable.wrapValue(self.firstName + " " + self.lastName)
        tokens.update(self.reservation.getTokens())
        return tokens
        



        
