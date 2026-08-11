class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        
        words = sentence.split(' ')
        result = []
        index = 1
        for i in words:
            ch = i[0].lower()
            if  ch == 'o' or ch == 'a' or ch == 'e' or ch == 'u' or ch == 'i':
                s =i + "ma"
            else: s = i[1:] + i[0] + "ma"
            
            s += "a" * index
            
            result.append(s)
            index += 1
            s = ""
        
        return ' '.join(result)
def main():
    sol = Solution()
    result = sol.toGoatLatin(sentence = "I speak Goat Latin")
    print(result)

if __name__ == "__main__":
    main()
                