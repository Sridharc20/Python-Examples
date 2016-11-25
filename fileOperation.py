#File operation

#open a file
fo = open("foo.txt","w")
#this will create a file if not exist.

fo.write("Python is a great language.\nYeah its great!!\n")

#close opened file
fo.close()