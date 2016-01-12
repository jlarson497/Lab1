import  string

userString = input("Please write your sentence here: ")
userString = string.capwords(userString, " ")
userString = userString.replace(" ", "")
firstLetter = userString[0]
firstLetter = firstLetter.lower()
userString = userString.replace(userString[0], firstLetter)
print((userString))