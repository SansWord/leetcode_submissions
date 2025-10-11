class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        days_of_month = {
             1: 31,
             2: 28,
             3: 31,
             4: 30,
             5: 31,
             6: 30,
             7: 31,
             8: 31,
             9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        # it's Friday in 1971/1/1
        days = 4

        # 365 % 7 is 1, and also consider leap years from 1971 to the last year
        days += (year - 1971) + self.leapYears(1971, year-1)

        # days of previous months of this year
        for m in range(1, month):
            days += days_of_month[m]

        # consider leap year of this year if already passed Feb.
        if month > 2 and self.isLeapYear(year):
            days += 1

        # days of this month
        days += day
        
        days %= 7

        return week_days[days]

    def isLeapYear(self, year: int) -> bool:
        if year % 4 == 0:
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            return True
        return False

    def leapYears(self, startYear, endYear) -> int:
        return sum([1 for i in range(startYear, endYear+1) if self.isLeapYear(i)])
