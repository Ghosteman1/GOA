#დამიწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ასაკს და სახელს.

#ხოლო დაუპრინტავს შემდეგი 10 წლის განმავლობაში რამდენი წლის იქნება ყოველ წელს 
#"ნიკა შენ იქნები 40 წლის 2024წელს"
#ნიკა შენ იქნები 41 წლის 2025 წელს" 
#და ა.შ

name = input("Enter Your Name: ")
age = int(input("Enter Your age: "))
year = int(input("Enter Year: "))

for i in range(10):
    print(name + " You will be " + str((age + i)) + " Years old in " + str(year + i))
