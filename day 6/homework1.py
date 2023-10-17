#დავალება:
#მომხმარებელს შეეკითხეთ ხელფასი
#თუ 10000ზე მეტია, დაუპრინტეთ, გოა-ში სწავლობდი?
#თუ 1000----10000 -ია , დაუპრინტეთ you mid
#თუ 1000-ზე დაბალია, დაუპრინტეთ, შემოსულიყავი გოაში, მატრიცელო

print(" Hello! ")
name = input("Enter your name: ")
surname = input("Enter your surname: ")
work = input("Where do you work?: ")
salary = int(input("How much is your salary?: "))
if salary > 10000:
    print(" Did you study in Goa-oriented acaddemy? ")
elif salary >=1000 and salary<=10000:
    print(" You mid. ")
elif salary <1000:
    print(" You studied in Goa and you would have a high salary... ")