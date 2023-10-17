#მომხმარებელს კითხეთ თავისი და მამამისის ასაკი, 
#დაუპრინტეთ ყოველ წელს რამდენჯერ უფროსი იქნება მამამისი მასზე.


name = input("Enter your name: ")
dad_name = input("Enter your Father name: ")
age = int(input("Enter your age: "))
dad_age = int(input("Enter your Father age: "))
year = int(input("Enter years: "))

for i in range(10):
    print(name + " Your father " + dad_name + " will be " + str((dad_age + i) / (age + i)) + " times older than you, in " + str(year + i))

