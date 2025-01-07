userString = input("Insert string:")

def reverse_string(x):
    newString = ""
    newSubString = ""

    for i in reversed(x.split()):           # Iterates through the string word-by-word in reverse order
        for j in reversed(i):               # Iterates through the substring letter-by-letter in reverse order
            newSubString += j               # Builds a new substring
        newString += newSubString + " "     # Builds a new string from each reversed substring
        newSubString = ""                   # Resets newSubString to empty for the next substring pass

    print(newString)

reverse_string(userString)