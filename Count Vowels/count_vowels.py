userString = input("Enter string:")
vowels = ['a', 'e', 'i', 'o', 'u']

def vowelCount(x):
    total_vowels = 0

    for i in x:
        if i in vowels:
            total_vowels += 1

    print("Number of 'a' encountered: " + str(x.count('a')))
    print("Number of 'e' encountered: " + str(x.count('e')))
    print("Number of 'i' encountered: " + str(x.count('i')))
    print("Number of 'o' encountered: " + str(x.count('o')))
    print("Number of 'u' encountered: " + str(x.count('u')))
    print("Total number of vowels: " + str(total_vowels))

vowelCount(userString)
