import random
print("Dice Roller")
while True:
    print("1. Roll a 6-sided die")
    print("2. Roll a 20-sided die")
    print("3. Roll multiple dice")
    print("4. Exit")
    choice=int(input("enter a choice:"))
    if choice==1:
        dice_rolled=random.randint(1,6)
        print(f"You rolled:",dice_rolled)
    elif choice==2:
        dice_rolled=random.randint(1,20)
        print(f"You rolled:" ,dice_rolled)
    elif choice==3:
        choice2=int(input("How many dice?"))
        rolls=[]
        
        for i in range(choice2):
            dice_rolled=random.randint(1,6)
            rolls.append(dice_rolled)
            
            
        print((f"You rolled: {dice_rolled}"))
        print(f"you rolled: {rolls}")
        
        
    elif choicce==4:
        print("bye")
        break
    else:
        print("invalid choice")
