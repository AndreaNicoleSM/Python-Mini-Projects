userString = input("Enter word:")

def checkPalindrome(x):
    x = x.lower()                                   # Make the string all lowercase letters to prevent errors in checking equivalence
    reversedString = ""
    for i in reversed(x):                           # Iterate through the string and build a new reversed string
        reversedString += i

    if x == reversedString:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

checkPalindrome(userString)