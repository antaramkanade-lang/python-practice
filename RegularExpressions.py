#Regular Expressions in Python=Its called "regex" for short,its a powerful tool for working with string and text data in python.They allow you to match and manipulate strings based on patterns,making it easy to perform complex string operations with just a few lines of code.
#It is imported by package re i.e import re.

#Metacharacters in Regular Expressions:- And there are many more characters except this ones.
# [] =Represent a character class.
# ^ =Matches the beginning.
# $ =Matches the end.
# . =Matches any character except newline.
# ? =Matches zero or one occurrence.
# | =Means OR
# * =Any no. of occurrence zero,one or more.
# + =One or more occurrences.
# {} =Indicate no. of occurrences of a preceding RE to match.
# () =Enclose a group of REs.

import re #this is used for importing package of Regular expressions.
pattern= r"[A-Z]+yclone" #here we need to find words in the paragraph having word "yclone" and starts with any capital letter and can be one or more and r is for printing raw string.
text='''A cyclone is a large-scale air mass that rotates around a strong low-pressure center,
        usually bringing clouds, wind, and precipitation.
        Cyclones spin counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere due to the Coriolis effect.
        The opposite system is called an anticyclone (maybe that's what you meant by Dyclone),
        which forms around a high-pressure center and typically brings clearer skies and more stable weather.
        While cyclones are associated with storms and unsettled conditions, anticyclones are linked to calm, dry weather patterns'''
#match=re.search(pattern,text) It is used to find first preference only and stops there.
matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(type(match.span()))
    print(match.span())
    print(text[match.span()[0]:match.span()[1]]) #this is used to print that two names of cyclone and dyclone.