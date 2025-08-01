listn = ["bachi", "machi", "gio"]
guess = []
counter = 0
while guess != listn:
    user_input = input("plz name:")
    if user_input in listn:
        print("u win")
        guess.append(user_input)
    else:
        print("try again")
        counter += 1
    if counter > 10:
           print("u lost")
           break
            
    if guess == listn:
            print("u win(2)")
            