#Homework 3
message = "If you want to hear a funny story, Sign up."

#Sign up
user_nickname = input("Your nickname: ")
name = input("Your name: ")
last_name = input("Your last name: ")
answer = input("Do you want continued? (yes/no)...")
message1 = input("You don't have other way, listen to me :D OK? ")

#funny story:
doctor = "Doctor: I’m sorry but you suffer from a terminal illness and have only 10 to live."
boy = "Patient: What do you mean by 10? 10 what? Years? Months? Weeks?!"
doctor_1 = "Doctor: Nine.."
boy_1 = "Patient: Whaaatttt????"
doctor_2 = "Doctor: Eight.."

#finish:
finish = input("Do you like this story? (Yes/no): ")
finish_message = "Thanks for attention. <3"

print(message, user_nickname, name, last_name, answer, message1, doctor, boy, doctor_1, boy_1, doctor_2, finish, finish_message)