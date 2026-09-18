def add(a, b):
    print(a+b)
add(5, 6)

def add(a=2, b=3):
    print(a+b)
add() 

def calculateGmean(a, b):
    print((a*b)/(a+b))

calculateGmean(b=8, a=9)

def average(*numbers): 
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum / len(numbers))

average(5,6,7,8)