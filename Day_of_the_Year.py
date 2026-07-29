class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        s = date.split('-')
        year, month, day = (int(s[0]), int(s[1]), int(s[2]))
        if (month < 2): return day

        result = 0
        for i in range(1, month):
           result = result + day_of_month[i]

        result = result + day

        return result
           

        

        
    def is_leap_year(year):
     if year % 400 == 0:
        return True
     if year % 100 == 0:
        return False
     if year % 4 == 0:
        return True
     return False

def main():
   sol = Solution()
   date = "2019-02-10"
   result = sol.dayOfYear(date)
   print(result)
if __name__ == "__main__":
   main()