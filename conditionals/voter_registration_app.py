from pickletools import read_int4

print("Welcome to the Voter Registration App")

name = input("\nPlease enter your name: ").title()
age = int(input("Please enter your age: "))
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

if age >= 18:
    print("\nCongratulations " + name + ", you are old enough to vote.")
else:
    print("Sorry, you're not old enough. Goodbye.")
    exit()

print("\nHere is a list of the political parties")
for item in parties:
    print("\t-", item)

party_choice = input("\nWhat party would you like to choose: ")

if party_choice in parties[:2]:
    print("\nCongratulations " + name + "! You have joined the " + party_choice + " party!")
    print("This is a major party.")
else:
    print("\nCongratulations " + name + "! You have joined the " + party_choice + " party!")
    print("This is not a major party.")