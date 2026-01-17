#readlines() method= it reads single line from the file if you want to make it read multiple lines then the loop is used and it returns a list of strings used when file is small and lines available at once
f=open('myfile.txt','r') #here we have printed the data which is stored in myfile.txt
while True:
    line=f.readline()
    print(line)
    if not line:
        print(line,type(line))
        break

f=open('thefile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline() #here readline is used because it reads one line at a time and returns a string. Its used when you want to process line by line
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"the marks of student {i} in maths is: {m1*2}")
    print(f"the marks of student {i} in english is {m2*2}")
    print(f"the marks of student {i} in SST is: {m3*2}")
    print(line)

#writelines() method= writes a sequence of strings to a file. The sequence can be any iterable object like list or a tuple
#the writelines() method does not add newline characters between the strings in the sequence. if you want to add newlines between strings then you can you a loop to write each string separately
f=open('thefile2.txt','w')
lines=['line 1\n','line 2\n','line 3\n','line 4\n']
f.writelines(lines)
f.close()