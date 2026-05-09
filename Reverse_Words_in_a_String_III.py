class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = ""
        word = s.split()
        for i in range(len(word)):
            rev = word[i][::-1]
            str += rev
            str = str + " "
        return  str
def main():
    sol = Solution()
    s = "Let's take LeetCode contest"
    result = sol.reverseWords(s)
    print(result)
if __name__ == "__main__":
    main()
            