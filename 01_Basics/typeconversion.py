price=input("Enter the price: ")
tax=input("Enter the tax: ")

net_price=float(price)*(1+float(tax)/100)
print("The net price is: ",net_price)