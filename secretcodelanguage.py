# write a secret code language
#Coding a secret code language= if we have a word less than 3 letters then just reverse it.But if we have a word more than 3 letters than we have to remove the first letter and append or add it to the last then we have to 3 random letters add them to last and 3 random letters to the first.
st=input("Enter the message:")
words=st.split(" ")
coding=True
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="jsh"
            r2="hrs"
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1]) #this is use to reverse a string
    print(" ".join(nwords))

#Decoding = we need to write coding=false here and write the jumbled statements in the output to make it straight using decoding
st=input("Enter the message:")
words=st.split(" ")
coding=False
if(coding):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="jsh"
            r2="hrs"
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
