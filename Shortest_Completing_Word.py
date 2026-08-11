class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        mymap = {}
        for i in licensePlate:
            if ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
                ch = i.upper()
                if ch in mymap: mymap[ch] += 1
                else: mymap[ch] = 1
        s = None
        for i in words:
            mapx = mymap.copy()
            for j in i:
                ch = j.upper()
                if ('A' <= ch <= 'Z'):
                    if ch in mapx: mapx[ch] -= 1
            if all(value <= 0 for value in mapx.values()):
                if s is None or (len(i) < len(s)): 
                    s = i
                  
            
        return s
def main():
    sol = Solution()
    licensePlate = "1s3 456"
    words = ["looks", "pest","stew","show"]
    result = sol.shortestCompletingWord(licensePlate, words)
    print (result)
if __name__ == "__main__":
    main()