class Solution(object):

    def titleToNumber(self, columnTitle):

        result = 0

        for ch in columnTitle:

            value = ord(ch) - ord('A') + 1

            result = result * 26 + value

        return result
def main():
  sol = Solution()
  col = "AC"
  result = sol.titleToNumber(col)
  print(result)
if __name__ == "__main__":
  main()  


