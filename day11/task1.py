print("Dear Diary")
thoughts=input("enter your thoughts")
with open("write.txt","a") as file:
    file.write(thoughts+"\n")
    print("Your thoughts have beeen saved")
