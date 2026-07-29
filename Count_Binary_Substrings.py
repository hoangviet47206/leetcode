class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # len = min(độ dài nhóm trước, độ dài nhóm sau)
        my_list = []

        tmp = 1
        for i in range(1, len(s)):
            if (s[i] == s[i - 1]): tmp = tmp + 1
            else: 
                my_list.append(tmp)
                tmp = 1
        my_list.append(tmp)
        result = 0
        for i in range(1, len(my_list)):
            result = result + min(my_list[i - 1], my_list[i])

        return result

def main():
    sol = Solution()
    s = "00110011"
    result = sol.countBinarySubstrings(s)
    print(result)
if __name__ == "__main__":
    main()


