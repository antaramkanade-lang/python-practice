#dictionaries= these are the ordered collection of elements separated with commas and enclosed with curly brackets and has key:value pairs
dict={
    344:"antara",
    56:"carla",
    285:"siri"
}
print(dict[285])
info={'name':'Antara','age':19,'eligibility':True}
print(info)
print(info['name'])
print(info.get('name')) #these are two methods we can access elements and this one with get doesnt give error it gives none in o/p if element is not present
print(info.keys()) #it will print all keys
print(info.values()) #it will print all its values of keys
for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
print(info.items())