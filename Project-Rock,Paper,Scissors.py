import random
user_score,comp_score=0,0
a,b,c="rock","paper","scissors"

while True:
    user_input=input("\nChoose :Rock,Paper,Scissor\nYour Choice:")
    comp_input=random.choice([a,b,c])

    if user_input.lower()==a:
        if comp_input==b:
            comp_score+=1
            print("\nYou Lose!")
        elif comp_input==c:
            user_score+=1
            print("\nYou Win!")
        elif comp_input==a:
            comp_score+=1
            user_score+=1
            print("\nIt's a Draw!")

    elif user_input.lower()==b:
        if comp_input==a:
            user_score+=1
            print("\nYou Win!")
        elif comp_input==c:
            comp_score+=1
            print("\nYou Lose!")
        elif comp_input==b:
            comp_score += 1
            user_score += 1
            print("\nIt's a Draw!")


    elif user_input.lower()==c:
        if comp_input==a:
            comp_score+=1
            print("\nYou Lose!")
        elif comp_input==b:
            user_score+=1
            print("\nYou Win!")
        elif comp_input==c:
            comp_score += 1
            user_score += 1
            print("\nIt's a Draw!")

    print("\nYour Score: ",user_score)
    print("Computer Score: ",comp_score)
    x=int(input("\nPress 1 to Play Again\nPress 2 to Exit :"))
    if x==1:
        continue
    elif x==2:
        break