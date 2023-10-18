#Homework 1
#Homework 1



#ბილეთი ღირს 25 ლარი, მაგრამ ბავშვებისთვის უფასოა,გვყავს 13 ადამიანი, 
#აქედან 10 დიდი და 3 ბავშვი, გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ 

age = int(input("Enter your age: "))
if age <=18:
    print("Entry is free for you...")
elif age >=18:
    print("Pay 25 GEL...")


tkt_price = 25
adults = 10
child = 3
print("Paid in full " + str(tkt_price * adults) + " GEL") #Paid in full
