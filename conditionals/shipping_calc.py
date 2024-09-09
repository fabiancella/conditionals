
print("Welcome to the Shipping Calculator App")

users = ["bob123", "robertk", "jimmyk", "bob1234"]
username = input("\nPlease enter your username: ")

if username in users:
    print("\nHello " + username + ", welcome back")
else:
    print("Sorry, username not found. Goodbye.")
    exit()

def shipping():
    ship1 = 5.10
    ship2 = 5.00
    ship3 = 4.95
    ship4 = 4.80
    return ship1, ship2, ship3, ship4
shipping_cost = shipping()

print("\nCurrent shipping prices are as follows:")
print("Shipping orders 0 to 100:\t\t\t\t$5.10 each")
print("Shipping orders 100 to 500:\t\t\t\t$5.00 each")
print("Shipping orders 500 to 1000:\t\t\t$4.95 each")
print("Shipping orders over 1000:\t\t\t\t$4.80 each")

items = int(input("\nHow many items would you like to ship: "))

if items in range(0, 100):
    print("Your shipment will cost:", items * shipping_cost[0], "at $5.10 per item")
elif items in range(100, 500):
    print("Your shipment will cost:", items * shipping_cost[1], "at $5.00 per item")
elif items in range(500, 1000):
    print("Your shipment will cost:", items * shipping_cost[2], "at $4.95 per item")
elif items in range(1000, 1000000):
    print("Your shipment will cost:", items * shipping_cost[3], "at $4.80 per item")
else:
    print("Invalid shipment")

confirm = input("\nWould you like to ship your package(s) (y/n): ").lower()

if "y" in confirm:
    print("\nOkay, your shipment is processing...")
    print("Shipping your", items, "items")
else:
    print("\nOkay have a nice day!")