num=78
guess=0
while(guess!=num):
	guess=int(input("Guess a number"))
	if (guess>num):
		print ("Too High")
	elif guess<num :
		print ("Too Low")
		
print ("Just right")