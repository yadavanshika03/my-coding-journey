letter="Hey my name is {} and I am from {}"
name="Anshika"
country="India"
print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")
print(f"we use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price=49.09999
txt=f"for only {price:.2f} dollars!"
print(txt)
print(txt.format())
print(type(f"{2*30}"))
