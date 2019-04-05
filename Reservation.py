from Tokenizable import Tokenizable

class Reservation(Tokenizable):
    def __init__(self, obj = None):
        self.roomNumber = "" #string - All the examples are numbers, but some hotels have letters in the room number so we account for future cases
        self.startTimestamp = None #POSIX - No default since we have no way to determine what a default would be
        self.endTimestamp = None #POSIX - No default since we have no way to determine what a default would be
        if obj:
            self.roomNumber = obj["roomNumber"] if "roomNumber" in obj else ""
            self.startTimestamp = obj["startTimestamp"] if "startTimestamp" in obj else None
            self.endTimestamp = obj["endTimestamp"] if "endTimestamp" in obj else None

    def getTokens(self):
        tokens = {}
        tokens["RESERVATION.ROOMNUMBER"] = Tokenizable.wrapValue(self.roomNumber)
        tokens["RESERVATION.STARTTIMESTAMP"] = Tokenizable.wrapValue(self.startTimestamp)
        tokens["RESERVATION.ENDTIMESTAMP"] = Tokenizable.wrapValue(self.endTimestamp)
        tokens["RESERVATION.DURATION"] = Tokenizable.wrapValue(self.endTimestamp - self.startTimestamp)
        return tokens
        