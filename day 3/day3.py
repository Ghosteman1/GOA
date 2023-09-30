#Ask the user for personal information 

name = input("Enter your name: ")
last_name = input("last name: ")
age = input("Enter your age: ")

#Calculate the user's age after 25 years
age1 = (int(age) + 25)

#Let's do everything together
print(("Your name is ") + name,  last_name, ("Your age is ") + str(age), ("And 25 years you will be ") + str(age1) +  ("years old"))