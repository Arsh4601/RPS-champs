import random as rd


def game(length,points,name,c1):

    options=["r","p","s","p","r","s","p","s","r","r","s","p"]
    choice=c1
    if(choice==2):

        player_won=0
        comp_won=0





    for i in range(1,length):

        comp_points=0
        player_point=0
        tie=0

        if(choice==2):

            print("\n Matches\n")
            print("Match  ",end='')
            print("Bot   ",end='')
            print(name )
            print(i-1,"     ",end='')
            print(comp_won,"     "  ,end='')
            print(player_won,"       ")
            print("\n")
            while True:

                ans=input("Do you wish to continue(y/n): ")

                if(ans=="y"):

                    break

                else:

                    print("Okay we'll wait for you :)")

            print("\nMatch",i)

        print("\nPoints\n")
        print("Match     ",end='')
        print("Bot     ",end='')
        print(name,"     "  ,end='')
        print("Ties  ")

        print(i,"        ",end='')
        print(comp_points,"      ",end='')
        print(player_point,"        "  ,end='')
        print(tie,"        ")
        print("\n")






        while True:

            c=rd.randint(0,11)
            comp_choice=options[c]
            print("\npress r for Rock")
            print("press p for paper")
            print("press s for scissor")
            print("\n")

            player_choice=input("rock,paper,or scissor: ")

            if(player_choice=="R" or player_choice=="r" or player_choice=="P" or player_choice=="p" or player_choice=="S" or player_choice=="s"):

                if(player_choice=="R" or player_choice=="r"):

                    player_choice="r"
                    print("You chose Rock")

                elif(player_choice=="P" or player_choice=="p"):

                    player_choice="p"
                    print("You chose paper")

                elif(player_choice=="S" or player_choice=="s"):

                    player_choice="s"
                    print("You chose scissor")

                if(comp_choice=="R" or comp_choice=="r"):

                    comp_choice="r"
                    print("Bot has choosen Rock\n")

                    while True:
                        ans=input("Do you wish to continue(y/n): ")

                        if(ans=="y"):

                            break

                        else:

                            print("Okay we'll wait for you :)")

                elif(comp_choice=="P" or comp_choice=="p"):

                    comp_choice="p"
                    print("Bot has choosen paper\n")

                    while True:

                        ans=input("Do you wish to continue(y/n): ")

                        if(ans=="y"):

                            break

                        else:

                            print("Okay we'll wait for you :)")

                elif(comp_choice=="S" or comp_choice=="s"):

                    comp_choice="s"
                    print("Bot has choosen scissor\n")

                    while True:

                        ans=input("Do you wish to continue(y/n): ")

                        if(ans=="y"):

                            break

                        else:

                            print("Okay we'll wait for you :)")


                if(player_choice==comp_choice):

                    print("Its a tie")
                    tie=tie+1


                elif(player_choice=="r"):

                    if(comp_choice=="p"):

                        print("Bot has won a point")
                        comp_points=comp_points+1

                    else:

                        print("You have won a point")
                        player_point=player_point+1


                elif(player_choice=="p"):

                    if(comp_choice=="s"):

                        print("Bot has won a point")
                        comp_points=comp_points+1

                    else:

                        print("You have won a point")
                        player_point=player_point+1


                elif(player_choice=="s"):

                    if(comp_choice=="r"):

                        print("Bot has won a point")
                        comp_points=comp_points+1

                    else:

                        print("You have won a point")
                        player_point=player_point+1

                print("\nPoints\n")
                print("Match  ",end='')
                print("Bot  ",end='')
                print(name,"  "  ,end='')
                print("Ties  ")

                print(i,"     ",end='')
                print(comp_points,"     ",end='')
                print(player_point,"     "  ,end='')
                print(tie,"       ")
                print("\n")

                while True:

                    ans=input("Do you wish to continue(y/n): ")

                    if(ans=="y"):

                        break

                    else:

                        print("Okay we'll wait for you :)")



                if(comp_points==points):

                    print("\nBot has won this match")
                    if(choice==2):

                        comp_won=comp_won+1

                    break

                elif(player_point==points):

                    print("\nCongratulations, you have won this match")

                    if(choice==2):

                        player_won=player_won+1

                    break



            else:

                print("Invalid choice,choose again\n")

        if(choice==2):

            if(i==3 and comp_won==3):

                print("\nBot has won the tournament")
                break

            elif(i==3 and player_won==3):

                print("\nCongratulations, you have won the tournament")

            elif(i==5 and comp_won>player_won):

                print("\nBot has won the tournament")
                break

            elif(i==5 and player_won>comp_won):

                print("\nCongratulations, you have won the tournament")
                break

            elif(i==4 and comp_won==3):

                print("\nBot has won the tournament")
                break

            elif(i==4 and player_won==3):

                print("\nCongratulations,you have won the tournament")
                break


                
print("Welcome to RPS Champs 2020")
print("Here you can have a friendly match of 10 points or ",end='')
print("Best of 5 tournament of 5 points each\n")

while True:

    n=input("Enter your name: ")
    try:

        n=int(n)
        print("Your name cant be numbers")

    except:

        break

while True:
    print("\nEnter 1 for a friendly match")
    print("Enter 2 for a Best of 5 tournament of 5 points each\n ")

    while True:

        choice=input("Your choice: ")

        try:

            choice=int(choice)

            if(choice==1 or choice==2):

                break

            else:

                print("Please enter either 1 or 2 only")

        except:

            print("Please enter either 1 or 2 only")



    if(choice==1):

        l1=2
        p1=10

    else:

        l1=6
        p1=5

    game(l1,p1,n,choice)

    print("\n")

    ans=input("Do you wish to continue (y/n): ")

    if(ans=="y" or ans=="Y" or ans=="n" or ans=="N"):

        if(ans=="n" or ans=="N"):

            break

    else:

        print("Please enter either y or n only")
