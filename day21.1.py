def greet(name):
    print(name)
greet("Anshika")

def greet(name = "Friend"):
    print(f"Hello {name}") 
greet("Anshika")

def calculateGmean(a, b):
    print((a*b)/(a+b))
calculateGmean(b=8, a=9)  

def add_all(*numbers): 
    print(sum(numbers))
add_all(1,2,3,4,5)
