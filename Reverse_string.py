def reverseString(string):
    reversedText = string[::-1]
    return reversedText

string = input("Enter a string: ")
reversedText = reverseString(string)
print("Original string: ", string)
print("Reversed string: ", reversedText)
