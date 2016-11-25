#read file 

#open a file
fo = open("foo.txt","r")

str = fo.read()

print ("File content \n",str)

fo.close()