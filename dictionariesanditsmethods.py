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
print(info.items()) #it will give all key value pairs togetherly

#dictionary methods= there are several built-in methods that used for manipulation of dictionaries
ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2) #it adds both the dictionaries in one using update
ep2.clear() #return an empty dict
print(ep1)
print(ep2)
ep1.pop(122) #pop removes this mentioned value from dictionary
print(ep1)
ep1.popitem() #popitem automatically removes the last key:value pair from dictionary
print(ep1)
del ep1[123] #del delets an entire dictionary if the one deleted pair is not mentioned
print(ep1)
