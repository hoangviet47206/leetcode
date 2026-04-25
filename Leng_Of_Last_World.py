class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for x in reversed(s.strip()):
            if x == " ":
             break
            count += 1

        return count

        