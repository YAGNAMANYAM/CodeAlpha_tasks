stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}
total_investment = 0
print("📈 Stock Portfolio Tracker")
print("\nAvailable Stocks and Prices:")
# Show available stocks
for stock in stock_prices:
    print(stock, ":", stock_prices[stock])
# Number of stocks
n = int(input("\nEnter number of stocks you want to add: "))
for i in range(n):
    print(f"\nStock {i+1}:")
    stock_name = input("Enter stock name: ").upper()
    if stock_name in stock_prices:
        print("Price of", stock_name, "is", stock_prices[stock_name])
        quantity = int(input("Enter quantity (number of shares): "))
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name} -> {quantity} x {stock_prices[stock_name]} = {investment}")
    else:
        print("❌ Stock not found!")
# Total
print("\n💰 Total Investment Value:", total_investment)