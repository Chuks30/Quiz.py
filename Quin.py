import random

#Intro message
print("Welcome to Where In The World Is The Civil ConFLiCT Trophy?")
print("Brought to you by Extra Points.")
user_name = input ("What is your name?")
print("Answer the following questions")
print("")
    
#question
question_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
user_score = 0
wrong_answer = "Sorry, that was incorrect."
right_answer = "Correct! To the next question!"

v = question_list.split(" ")
while random.choice < len(v):
#while computer_action < 20:
  computer_action = random.choice(question_list)
   if computer_action == 1:
    print("Echo is on the run towards the school with the smallest enrollment in FBS. Where should we go?")
    print("A. Navy.")
    print("B. Tulsa.")
    print("C. SMU.")
    print("D. Rice.")
    user_answer_1 = input("Please answer A, B, C or D.")
     if user_answer_1 == "B":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)
           

   elif computer_action == 2:
    print("What is the name of our python facilitator.")
    print("A. Precious")
    print("B. Chibuzo")
    print("C. Kim")
    print("D. Grace")
    user_answer_2 = input("Please answer A, B, C or D.")
    if user_answer_2 == "A":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 3:
    print("How many state are there in Nigeria! ")
    print("A. 25.")
    print("B. 30.")
    print("C. 36.")
    print("D. 48.")
    user_answer_3 = input("Please answer A, B, C or D.")
    if user_answer_3 == "C":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)
        

elif computer_action == 4:
    print("Who is our java facilitator.")
    print("A. Grace and Chibuzo")
    print("B. Precious")
    print("C. Kim")
    print("D. Cubaner")
    user_answer_4 = input("Please answer A, B, C or D.")
    if user_answer_4 == "A":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)
        

elif computer_action == 5:
    print("Which animal is the king of the jungul. ")
    print("A. Goat")
    print("B. Monkey")
    print("C. Rat")
    print("D. Lion")
    user_answer_5 = input("Please answer A, B, C or D.")
    if user_answer_5 == "D":
        print(right_answer)
        user_score +1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 6:
    print("When did nigeria got their independent.")
    print("A. 2 jun.")
    print("B. 1 october.")
    print("C. 92 september.")
    print("D. 185 may.")
    user_answer_6 = input("Please answer A, B, C or D.")
    if user_answer_6 == "B":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)
        

elif computer_action == 7:
    print("Football is a game of!")
    print("A. Work.")
    print("B. Hard.")
    print("C. Luck.")
    print("D. Any how.")
    user_answer_7 = input("Please answer A, B, C or D.")
    if user_answer_7 == "C":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 8:
    print("School is a place of.")
    print("A. Playing.")
    print("B. Praying.")
    print("C. Jump jump.")
    print("D. Learing.")
    user_answer_8 = input("Please answer A, B, C or D.")
    if user_answer_8 == "D":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 9:
    print("Who created heven and earth.")
    print("A. James.")
    print("B. God.")
    print("C. Texas Tech.")
    print("D. Wilson.")
    user_answer_9 = input("Please answer A, B, C or D.")
    if user_answer_9 == "B":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 10:
    print("How many native are in c15.")
    print("A. 102.")
    print("B. 4.")
    print("C. 29.")
    print("D. All of the above.")
    user_answer_10 = input("Please answer A, B, C or D.")
    if user_answer_10 == "C":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 11:
    print("What is the square of 10")
    print("A. 100.")
    print("B. 82.")
    print("C. 60.")
    print("D. 12.")
    user_answer_11 = input("Please answer A, B, C, or D.")
    if user_answer_11 == "A":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 12:
    print("Who ate the apple in iPhone.")
    print("A. Adam.")
    print("B. Eve.")
    print("C. Iphone company.")
    print("D. All of the above.")
    user_answer_12 = input("Please answer A, B, C or D.")
    if user_answer_12 == "C":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 13:
    print("What does str in python represent.")
    print("A. Integer.")
    print("B. String.")
    print("C. void.")
    print("D. Non of the above")
    user_answer_13 = input("Please answer A, B, C, or D.")
    if user_answer_13 == "B":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 14:
    print("What is the square root of 25.")
    print("A. 50.")
    print("B> 32.")
    print("C. 85.")
    print("D. 5.")
    user_answer_14 = input("Please answer A, B, C, or D.")
    if user_answer_14 == "D":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 15:
    print("2 multiplied br 4.")
    print("A. 8.")
    print("B. 22.")
    print("C. 30.")
    print("D. 2.")
    user_answer_15 = input("Please answer A, B, C or D.")
    if user_answer_15 == "A":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 16:
    print("2 multiplied br 10.")
    print("A. 8.")
    print("B. 22.")
    print("C. 20.")
    print("D. 2.")
    user_answer_16 = input("Please answer A, B, C or D.")
    if user_answer_16 == "C":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 17:
    print("12 multiplied br 4.")
    print("A. 8.")
    print("B. 22.")
    print("C. 30.")
    print("D. 48.")
    user_answer_17 = input("Please answer A, B, C or D.")
    if user_answer_17 == "D":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 18:
    print("2 multiplied br 7.")
    print("A. 14.")
    print("B. 22.")
    print("C. 30.")
    print("D. 2.")
    user_answer_18 = input("Please answer A, B, C or D.")
    if user_answer_18 == "A":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 19:
    print("6 multiplied br 4.")
    print("A. 8.")
    print("B. 22.")
    print("C. 24.")
    print("D. 2.")
    user_answer_19 = input("Please answer A, B, C or D.")
    if user_answer_19 == "C":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)

elif computer_action == 20:
    print("4 multiplied br 4.")
    print("A. 16.")
    print("B. 22.")
    print("C. 30.")
    print("D. 2.")
    user_answer_20 = input("Please answer A, B, C or D.")
    if user_answer_20 == "A":
        print(right_answer)
        user_score + 1
        computer_action = random.choice(question_list)
    else:
        print(wrong_answer)


        
if user_score == 15:
    print("Congrats!.")
    print("")