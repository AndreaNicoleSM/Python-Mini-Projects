def menu():
        print("Welcome to the Python Word Counter")
        choices={                   #Dictionary for choices
            1:"Enter String" ,
            2:"Read from txt",
        }
        for i in choices.keys():    #For loop iterates through choices dictionary to print the menu. Allows for scaling later.
            print(f"{i} - {choices[i]}")
        arg=int(input("Please Choose : "))
        R=choices.get(arg,-1)
        if R==-1:               #Validation checking
            print("\n Invalid Choice ! Try again ....\n")
            menu()
        else:
            print(f"You Chose: {R}")
            if arg==1:
                countString()   #If chosen, user inputs a string manually and the words are counted.
            if arg==2:
                countTxt()      #If chosen, words are counted from input.txt

def countString():
    userString = input("Enter String:")
    print("Length of string: " + str(len(userString.split())))

def countTxt():
     text = open("Python Mini Projects\Count Words in String\input.txt", "r")
     print("Length of string: " + str(len(text.read().split())))
     text.close()
     

menu()