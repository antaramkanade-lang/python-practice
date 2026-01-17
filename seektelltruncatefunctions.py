#seek() and tell() functions= these are used to work with file objects and their positions within a file.these functions are the part of built-in IO module which provides a consistent interface for reading and writing to various file-like objects such as files,pipes & in-memory buffers
# seek() function:- it allows to move the current position within a file to a specific point.The position is specified in bytes & you can move either forward or backward from the current position
with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(10) #here seek 10 means move to the 10th byte of the sentence in myfile.txt
    data=f.read(5) #here read 5 means read the next 5 bytes
    print(data)

#tell() function:- it tells till how many bytes we have applied seek() function like in above example we have done seek(10) so it will print 10 in o/p so that we know till that byte we seek the letters
with open('myfile.txt','r') as f:
    print(type(f))
    f.seek(9)
    print(f.tell()) #here it will print 9 to tell the no. of bytes till we used seek function
    data=f.read(6)
    print(data)

#truncate() function:- by using this functions we can tell that how many letters or bytes we want to take in our file
with open('sample.txt','w') as f: #we made this file and writing in it
    f.write('I am the one and only person in the world whon knows python properly!!!!!!!!!!')
    f.truncate(20) #here this truncate will only print 20 bytes in the file from the whole sentence
with open('sample.txt','r') as f:
    print(f.read())