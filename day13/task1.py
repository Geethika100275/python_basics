import random

while True:
    print("\nDice Roller")
    print("1. Roll a 6-sided die")
    
    print("2. Roll a 20-sided die")
    print("3. Roll multiple dice")
    print("4. Exit")

    choice = input("Choose option: ")

    
    
    
    if choice == "1":
        print("🎲 You rolled:", random.randint(1, 6))
    elif choice == "2":
        print("🎲 You rolled:", random.randint(1, 20))
    elif choice == "3":
        n = int(input("How many dice? "))
        rolls = [random.randint(1, 6) for i in range(n)]
        print("🎲 You rolled:", rolls)
        print("Total:", sum(rolls))
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
