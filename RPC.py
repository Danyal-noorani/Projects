import random
selection =""

# Computer's Opttions
lst = ["R",
       "P",
       "S"]
cwin = 0
pwin = 0
draw=0
while selection!="E":
    #User Options
    choice = input("[R]ock\n[P]aper\n[S]cissor\nEnter your choice: ")
    choice = choice.upper()
    c_choice = random.choice(lst)

    #Logic

    print(f"{choice} vs {c_choice}")
    if choice == c_choice:
        print("Draw")
        draw+=1

    elif choice == "R" and c_choice =="S" or choice == "S" and c_choice =="P" or choice == "P" and c_choice =="R":
        print("Player has won")
        pwin+=1

    elif c_choice == "R" and choice =="S" or c_choice == "S" and choice =="P" or c_choice == "P" and choice =="R":
        print("Computer has won")
        cwin+=1

    print(f"\tScore\nPlayer:\t\t{pwin}\nComputer:\t{cwin}\nDraw\t\t{draw}")
    selection = input("[P]lay again \n[E]xit\n: ")
    selection = selection.upper()
