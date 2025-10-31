print("File Reader")

while True:
    filename = input("Enter filename: ").strip()

    
    try:
        with open(filename, 'r') as file:
            print("File contents:")
            print(file.read())
            break  # Exit after successfully reading the file
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        retry = input("Would you like to try another file? (y/n): ").strip().lower()
        if retry != 'y':
            print("Exiting program.")
            break

    