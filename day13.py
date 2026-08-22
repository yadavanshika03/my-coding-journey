# Strings are immutable
a="!!!!Anshika!!!!! !!!!!!!!!!!!! Anshika"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Anshika","Angel"))
print(a.split(" "))
blogHeading="introduction to js"
print(blogHeading.capitalize())

str1="Welcome to the Console!!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Anshika"))

str1="Welcome to the Console!!!!"
print(str1.endswith("!!!!"))

str1="Welcome to the Console!!!!"
print(str1.endswith("to",4,10))

str1="He's name is Dan. He is an honest man."
print(str1.find("ishhh"))
#print(str1.index("ishhh"))

str1="WelcomeToTheConsole"
print(str1.isalnum())
str1="Welcome"
print(str1.isalpha())

str1="hello world"
print(str1.islower())

str1="we wish you a marry christmas\n"
print(str1.isprintable())
str1="               "      
print(str1.isspace())
str2="   "
print(str2.isspace())

str1="World Health Organisation"
print(str1.istitle())

str2="world health organisation"
print(str2.istitle())

str1="Python is a Interpreted Language"
print(str1.startswith("Python"))

str1="Python is a Interpreted Language"
print(str1.swapcase())

str1="His name is Dan.Dan is an honest man."
print(str1.title())





