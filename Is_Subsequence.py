class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        fregS = self.tansuat(s)
        fregT = self.tansuat(t)
        
        dem = 0
        for char, value in fregS.items():
            if char in fregT and value <= fregT[char]:
                dem = dem + 1
        print(dem)
        return dem == len(s)
    
    def tansuat(self, a):
        freg = {}
        for i in a:
            freg[i] = freg.get(i, 0) + 1       
        return freg

def main():
    sol = Solution()
    result = sol.isSubsequence(s ="acb", t = "ahbgdc")
    print(result)
if __name__ == "__main__":
    main()