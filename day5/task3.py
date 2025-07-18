manager = []
while True:
    print("\n1.Add item")
    print("2.Remove item")
    print("3.Show list")
    print("4.Check item")
    print("5.Exit")
    choice = (int(input("Enter the choice")))
    if choice==1:
        item=input("enter the item to add:")
        manager.append(item)
        print(manager)
        print(f"Added {item}")
    elif choice==2:
        item=input("Enter the item to remove:")
        manager.remove(item)
        print(f"Removed {item}")
    elif choice==3:
        print(manager)
    elif choice==4:
        item=input("Enter the item to check:")
        if item in manager:
            print("item is in the manager")
        
        else:
            print("item not in manager")
    elif choice==5:
        print("Exiting")
    
