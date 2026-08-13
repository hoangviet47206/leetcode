class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s) // 2 + 1):
            ch = s[:i]
            if s == ch * (len(s) // len(ch)): return True
        
            
        return False

def main():
    sol = Solution()
    s = "aba"
    result = sol.repeatedSubstringPattern(s)
    print(result)
if __name__ == "__main__":
    main()
    