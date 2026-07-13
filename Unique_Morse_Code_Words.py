class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        character = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for i in words:
            s = ""
            for j in i:
                s += character[ord(j) - ord('a')]
            if s not in seen:
                seen.add(s)

        return len(seen)        

def main():
    sol = Solution()

    words = ["gin", "zen", "gig", "msg"]

    result = sol.uniqueMorseRepresentations(words)
    print(result)


if __name__ == "__main__":
    main()