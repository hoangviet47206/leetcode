class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        s = set(jewels)

        index = 0
        for i in stones:
            if i in s:
                index += 1

        return index        