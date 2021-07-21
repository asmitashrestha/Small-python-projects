name=input("Enter your name:")
print("Welcome",name,"to this journey!!")

option=input("Are you excited(yes/no)?")
if option!="yes":
    quit()

print("Okay then be ready for longdrive and you will be surprise at last!!")

answer=input("You met a stranger on the way he asked for lift.Do you want to give him a lift(y/n)?").lower()
if answer=="y":
    print("You will have fun in a way and of course stranger will give you a gift!")
    answer=input("He will asked you for a dinner.Would you like to go(yeah/naa)?")

    if answer=="yeah":
        print("Stranger really get impressed by you and fall in love with you!!")
        answer= input("He proposed you for a engagement.What would be your answer(ok/notok)?")
        if answer=="ok":
            print("You will be surprised after marriage because he is one of the most popular business man in the world and obviously he loves you unconditionally!!")

        else:
            print("It's your bad luck you lose the chance to have such a honest man as your life partner!")

    else:
         print("You have missed the golden opportunity !!")

else:
    print("Oh shit!!You lose the chance to know about that person.") 

print("Congratulations",name,"for having this beautiful journey!!")    





