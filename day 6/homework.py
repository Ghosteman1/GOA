#მომხმარებლის ნიშნებისგან გამოანგარიშება საშუალო არითმეტიკული და თუ ცხრაზე მეტი იქნება:
#დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები
#თუ ეს იქნება 5ზე ნაკლები: დაუპრინტე გილოცავ გაექეცი მატრიცას
#თუ იქნება 5 იდან 9 მდე: დაუპრინტე YOU ARE MID
#თუ იქნება 10ზე მეტი ან 0ზე ნაკლები: დაუპრინტე there is something wrong with you

results1 = int(input("Enter your avarage: "))
results2 = int(input("Enter your avarage: "))
results3 = int(input("Enter your avarage: "))
results4 = int(input("Enter your avarage: "))
results5 = int(input("Enter your avarage: "))

avg_score = (results1 + results2 + results3 + results4 + results5) / 5 #საშუალო არითმეტიკული

if avg_score > 9 and avg_score <=10:
    print(" გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები! :) ")
elif avg_score <5:
    print(" გილოცავ გაექეცი მატრიცას! :) ")
elif avg_score >= 5 and avg_score <=9:
    print(" YOU ARE MID. ")
elif avg_score > 10 or avg_score <0:
    print(" there is something wrong with you... ")
print(" Well done! ")


