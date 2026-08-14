class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        tmp = s.upper().split('-')
        joined = "".join(tmp)
        
        if len(joined) <= k: return joined
        n = len(joined) // k
        tmp = len(joined) - n * k
        if tmp > 0:
           result = joined[0:tmp] + "-"
        else:
           result = ""
        for i in range(tmp, len(joined), k):
            result = result + joined[i:i+k]
            if(i + k != len(joined)):
                result = result + "-"
        
        return result
            
        
def main():
    sol = Solution()
    result = sol.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4)
    print(result)
    
if __name__ == "__main__":
    main()