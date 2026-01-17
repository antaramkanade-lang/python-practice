#String Formatting= it is done by using the format method
#f-strings in python
letter="Hey my name is {} and I am from {}"
country="India"
name="Antara"
print(letter.format(name,country)) #By format method
print(f"Hey my name is {name} and I am from {country}")#By fstring
price=49.09999
txt=f"For only {price:.2f} dollars!" #this 2f is used for taking the whole no. means for 49.09999 we take 49.10
print(txt)
st="The motive of our nation is {} and the demonstration is made up by the {}"
moto="Cleanliness"
demon="government"
print(st.format(moto,demon))
print(f"The motive of our nation is {moto} and the demonstration is made up by the {demon}")

print(f"{2*30}")