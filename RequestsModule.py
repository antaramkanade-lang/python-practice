#HTTP = HyperText Transfer Protocol.It’s just a set of rules for:sending a request and receiving a response.
#Requests module in python=Its a HTTP library that enables developers to send HTTP requests using python codes and makes it possible to interact with APIs and web services.
#For making it run in computer i installed this(C:\Users\antar\AppData\Local\Programs\Python\Python314\python.exe -m pip install requests) by entering it into cmd prompt.

import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":'Antara',
    "body":'Mam',
    "userId":12,
}
headers={
    'Content-type':'application/json; charset=UTF-8',
}
response=requests.post(url,headers=headers,json=data)
print(response.text)

#By printing this code it will give the html source code of this page:-
import requests
url="https://www.codewithharry.com/blogpost/django-cheatsheet"
r=requests.get(url)
print(r.text)

#bs4 Module=There is another module called Beautiful Soup which is used for web scraping in python.Its used for pulling data outside of HTML and XML files.It works with your fav parser to provide idiomatic ways of navigating,searching and modifying the parse tree.it commonly saves programmers hours or days of work.
#First I installed Beautiful Soup in my python using this (C:\Users\antar\AppData\Local\Programs\Python\Python314\python.exe -m pip install beautifulsoup4) entering in the cmd prompt.
import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com/blogpost/django-cheatsheet/"
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)