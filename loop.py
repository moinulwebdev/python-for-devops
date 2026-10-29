fruits = ["Banana", "Lichi", "Mango", "Apple"]

for item in fruits:
    print(item)


prices = [1.50, 4.99, 10.00, 25.50]

cents_prices = []

for item in prices:
    item = int(item * 100)
    cents_prices.append(item)
# print(cents_prices)


dollar_prices = [1.50, 4.99, 10.00, 25.50]

cents_prices = [int(item * 100) for item in dollar_prices]

print(cents_prices)

# # One single line replaces the 4 lines of code above
# cents_prices = [int(price * 100) for price in dollar_prices]
