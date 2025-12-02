n = int(input("Enter the number of items: "))
bill = 0

for i in range(1, n + 1):
    price = int(input(f"Enter the price of item {i}: "))
    bill = bill + price

print("Total bill =", bill)
