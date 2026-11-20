
import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 190
}

total_investment = 0
portfolio = []

print("WELCOME TO STOCK PORTFOLIO TRACKER")

while True:

    stock = input("\nEnter stock name: ").upper()

    if stock in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            price = stock_prices[stock]
            value = price * quantity

            total_investment += value

            portfolio.append([stock, quantity, price, value])

            print("Stock:", stock)
            print("Price:", price)
            print("Investment value:", value)
        else:
            print("Enter a valid quantity.")

    else:
        print("Stock not available!")

    choice = input("\nAdd another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n----- PORTFOLIO SUMMARY -----")

for item in portfolio:
    print(item[0], "Quantity:", item[1],
          "Value:", item[3])

print("Total Investment:", total_investment)

with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Stock", "Quantity", "Price", "Value"])
    writer.writerows(portfolio)

print("\nPortfolio saved successfully!")
