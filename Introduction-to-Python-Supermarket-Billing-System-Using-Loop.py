n = int(input("Enter the number of items:"))
bill=0
for i in range (0,n):
    price=int(input("Enter the price:"))
    bill=bill+price
print("Total bill=",bill)
