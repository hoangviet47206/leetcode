class Solution(object):
    def reverseStr(self, s, k):

        s = list(s)

        # mỗi lần nhảy 2k ký tự
        for i in range(0, len(s), 2 * k):

            # đảo k ký tự đầu
            left = i
            right = min(i + k - 1, len(s) - 1)

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return ''.join(s)


def main():
    sol = Solution()
    result = sol.reverseStr("abcdefg", 2)
    print(result)


if __name__ == "__main__":
    main()