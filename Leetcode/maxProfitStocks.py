# def Stock(prices):
#     max_profit = 0
    
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[j] - prices[i] > max_profit:
#                 max_profit = prices[j] - prices[i]
#     return max_profit


def Stock(prices):
    minPrice = prices[0]
    maxProfit = 0
    
    for price in prices:
        minPrice = min(minPrice, price)
        
        profit = price - minPrice
        
        maxProfit = max(maxProfit, profit)
    return maxProfit
prices = []
n = int(input())
for i in range(0,n):
    prices.append(int(input()))
print(Stock(prices))