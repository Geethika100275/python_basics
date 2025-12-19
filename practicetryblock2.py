ry:
    with open("kunju.txt", "a") as file:
        file.write("\nkunju is good ")
except PermissionError:
    print("Cannot write to 'kunju.txt'. Check permissions or folder.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

while True:
    print("\nfile reader")
    try:
       
        name=input("enter a filename").strip()
        with open(name,"r") as file:
                
            content=file.read()
            print(content)
    except FileNotFoundError:
        print(f"{name} is not found")
    except PermissionError:
        
        print(f"Permission denied to access {name}")
    choice= input("you wanna stop?")
    if choice=="yes":
        
        break
