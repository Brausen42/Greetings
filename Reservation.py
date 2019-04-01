from Tokenizable import Tokenizable

class Reservation(Tokenizable):
    def __init__(self, obj = None):
        self.roomNumber = None #string
        self.startTimestamp = None #Number
        self.endTimestamp = None #Number
        if obj:
            self.roomNumber = obj["roomNumber"] if "roomNumber" in obj else None
            self.startTimestamp = obj["startTimestamp"] if "startTimestamp" in obj else None
            self.endTimestamp = obj["endTimestamp"] if "endTimestamp" in obj else None

    def getTokens(self):
        tokens = {}
        tokens["RESERVATION.ROOMNUMBER"] = lambda tokens : str(self.roomNumber)
        tokens["RESERVATION.STARTTIMESTAMP"] = lambda tokens : str(self.startTimestamp)
        tokens["RESERVATION.ENDTIMESTAMP"] = lambda tokens : str(self.endTimestamp)
        return tokens
        