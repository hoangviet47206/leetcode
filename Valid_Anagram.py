class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)): return False
        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(s[i]) - ord('a')] += 1
            arr[ord(t[i]) - ord('a')] -= 1

        return all(x == 0 for x in arr)
def main():
    sol = Solution()
    s = "abca"
    t = "gjsg"
    result = sol.isAnagram(s, t)
    print(result)

if __name__ == "__main__":
    main()