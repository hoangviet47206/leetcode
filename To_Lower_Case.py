class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = ""
        for c in s:
            if 'A' <= c <= "Z":
                result += chr(ord(c) + 32)
            else:
                result += c

        return result

sol = Solution()

s = input("Nhập chuỗi: ")
print(sol.toLowerCase(s))