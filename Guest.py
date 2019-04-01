from Tokenizable import Tokenizable
from Reservation import Reservation

class Guest(Tokenizable):
    def __init__(self, obj = None):
        self.id = None #string
        self.firstName = "" #string
        self.lastName = "" #string
        self.reservation = Reservation() #Reservation
        if obj:
            self.id = obj["id"] if "id" in obj else None
            self.firstName = obj["firstName"] if "firstName" in obj else None
            self.lastName = obj["lastName"] if "lastName" in obj else None
            if "reservation" in obj:
                self.reservation = Reservation(obj["reservation"])

    def getTokens(self):
        tokens = {}
        tokens["GUEST.FIRSTNAME"] = lambda tokens : str(self.firstName)
        tokens["GUEST.LASTNAME"] = lambda tokens : str(self.lastName)
        tokens.update(self.reservation.getTokens())
        return tokens
        



        
