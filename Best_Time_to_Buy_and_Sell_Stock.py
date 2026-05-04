class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        result = 0
        for i in range(len(prices)):
            if (prices[i] < min_price):
                min_price = prices[i]
            else:
                result = max(result, prices[i] - min_price)
        
        return result 

def main():
   sol = Solution()
   prices = [7,1,5,3,6,4]         
   result = sol.maxProfit(prices)
   print(result)

if __name__ == "__main__":
   main() 