class Solution(object):
    def intToRoman(self, num):
        s = ""

        if num >= 1000:
            k = num // 1000
            s += k * 'M'
            num %= 1000

        if num >= 900:
            s += 'CM'
            num -= 900
        elif num >= 500:
            s += 'D'
            num -= 500

        if num >= 400:
            s += 'CD'
            num -= 400
        elif num >= 100:
            k = num // 100
            s += k * 'C'
            num %= 100

        if num >= 90:
            s += 'XC'
            num -= 90
        elif num >= 50:
            s += 'L'
            num -= 50

        if num >= 40:
            s += 'XL'
            num -= 40
        elif num >= 10:
            k = num // 10
            s += k * 'X'
            num %= 10

        if num == 9:
            s += 'IX'
        elif num >= 5:
            s += 'V'
            num -= 5
            s += 'I' * num
        elif num == 4:
            s += 'IV'
        else:
            s += 'I' * num

        return s
def main():
    sol = Solution()
    result = sol.intToRoman(num =3749 )
    print(result)
if __name__ == "__main__":
    main()