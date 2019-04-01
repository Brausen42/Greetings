from datetime import datetime, timedelta, timezone

# Supports US timezones currently
class Timezone:
    def __init__(self, name="US/Central"):
        self.name = name
        if self.name == "US/Eastern":
            self.timezone = timezone(timedelta(hours=-5))
        elif self.name == "US/Central":
            self.timezone = timezone(timedelta(hours=-6))
        elif self.name == "US/Mountain":
            self.timezone = timezone(timedelta(hours=-7))
        elif self.name == "US/Pacific":
            self.timezone = timezone(timedelta(hours=-8))

    def getTimeOfDay(self, time): # where 'time' is a 'datetime' object
        hour = datetime.fromtimestamp(time.timestamp(), tz=self.timezone).hour
        if hour < 12:
            return "Morning"
        if hour < 16:
            return "Afternoon"
        return "Evening"