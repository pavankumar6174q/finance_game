print("welcome to finance game made by an amatuare:>")
print("you are a working person and wanna get out of the rat race and enjoy your retirement")
option1 = input("Do you wanna buy a 'car or 'house\n").lower()
if option1 == 'house':
    print("good decision cause its an asset")
    option2=input("which one is better 'FD' or 'STOCK'\n ").lower()
    if option2 ==  'stock':
        print("good ")
        option3=input('you are enjoying profits of stocks do you "use" or "reinvest"\n  ').lower()
        if option3=="reinvest":
             print("congrats you have cracked the code$$")
        else:
            print("not a wise decision think again......")
    
    else:
        print("fd is nice but nt so useful")
else:
    print("game over cause its a liability")