class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        word = s.split()                 # tách thành các từ (mặc định " ")
        for i in range(len(word)):
            rev = word[i][::-1]          # đảo ngược các từ 
            result.append(rev)
        return " ".join(result)          # thêm vào và cách nhau bằng " "
def main():
    sol = Solution()
    s = "Let's take LeetCode contest"
    result = sol.reverseWords(s)
    print(result)
if __name__ == "__main__":
    main()
            