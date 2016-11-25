count_n=0
count_x=0
for n in range(2,10): # 2 to 9
	count_n+=1
	print("n is ",n)
	for x in range(2,n): # 2 to (n-1)
		count_x+=1
		print("x is ",x)
		if (n%x==0):
			print(n,'equals',x , '*',n/x)
			break
		else:
			print(n,"is a prime number")
print("End of loop ,count_n=",count_n , "count_x",count_x)

#Output 			
#n is  2
#n is  3
#x is  2
#3 is a prime number
#n is  4
#x is  2
#4 equals 2 * 2.0
#n is  5
#x is  2
#5 is a prime number
#x is  3
#5 is a prime number
#x is  4
#5 is a prime number
#n is  6
#x is  2
#6 equals 2 * 3.0
#n is  7
#x is  2
#7 is a prime number
#x is  3
#7 is a prime number
#x is  4
#7 is a prime number
#x is  5
#7 is a prime number
#x is  6
#7 is a prime number
#n is  8
#x is  2
#8 equals 2 * 4.0
#n is  9
#x is  2
#9 is a prime number
#x is  3
#9 equals 3 * 3.0
#End of loop ,count_n= 8 count_x 14