from datetime import datetime, timedelta

class CustomDT:
    def __init__(self, year=None, month=None, day=None, hour=0, minute=0, second=0):
        if year is None:
            now = datetime.utcnow()
            self.date = datetime(now.year, now.month, now.day, hour, minute, second)
        else:
            self._validate_date(year, month, day)
            self.date = datetime(year, month, day, hour, minute, second)

    @classmethod
    def validate_date(cls, year, month, day):
        try:
            cls._validate_date(year, month, day)
            return True
        except ValueError as e:
            return str(e)

    @staticmethod
    def _validate_date(year, month, day):
        datetime(year, month, day)

    @classmethod
    def date_difference(cls, date1, date2, unit='days'):
        delta = date2.date - date1.date
        if unit == 'weeks':
            return delta.days // 7
        elif unit == 'months':
            return cls.difference(date1.date, date2.date)
        else:
            return delta.days

    @staticmethod
    def difference(date1, date2):
        return (date2.year - date1.year) * 12 + date2.month - date1.month

    @classmethod
    def from_iso_format(cls, iso_string):
        try:
            date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S")
            return cls(date.year, date.month, date.day, date.hour, date.minute, date.second)
        except ValueError as e:
            raise ValueError("Invalid ISO 8601 format: {}".format(e))

    def to_iso_format(self):
        return self.date.strftime("%Y-%m-%dT%H:%M:%S")

    def to_human_readable_format(self):
        return self.date.strftime("%B %d, %Y %H:%M:%S")


if __name__ == "__main__":

    dt1 = CustomDT()  
    dt2 = CustomDT(2023, 1, 15, 10, 30, 45)  
    dt3 = CustomDT(2023, 1, 15)  


    print("ISO Format:", dt1.to_iso_format())
    print("Human Readable Format:", dt1.to_human_readable_format())

    

   # iso_string = "2023-01-15T10:30:45"
    #dt4 = CustomDT.from_iso_format(iso_string)

