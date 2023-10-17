#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you

name = input("Enter your name: ") #user name
surname = input("Enter your surname: ") #user surname
results = int(input("Enter your results: ")) #user results
if results > 9:
    print(" გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები! :) ")
elif results <5:
    print(" გილოცავ გაექეცი მატრიცას! :) ")
elif results >= 5 and results <=9:
    print(" YOU ARE MID. ")
elif results > 10 or results <0:
    print(" there is something wrong with you... ")
print(" Well done! ")


