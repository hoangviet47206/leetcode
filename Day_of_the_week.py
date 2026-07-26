from datetime import datetime

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        date = datetime(year, month, day)
        weekday = date.weekday()

        if weekday == 0:
            return "Monday"
        elif weekday == 1:
            return "Tuesday"
        elif weekday == 2:
            return "Wednesday"
        elif weekday == 3:
            return "Thursday"
        elif weekday == 4:
            return "Friday"
        elif weekday == 5:
            return "Saturday"
        else:
            return "Sunday"