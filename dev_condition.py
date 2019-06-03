print ("This is an example of conditions in Python")

for i in range(5):
	x = int(input("What's your age: "))
	print ("Thanks for letting us know your age", end=":")

	if x < 0 or x > 120 :
		print("Sorry Invalid Entry, Please try again")
	elif x < 3 :	
		print(" Well so you are a Baby")
	elif x < 5 :
		print(" Well so you are a Todller")
	elif x < 15:
		print(" Well so you are a Young Boy")
	elif x < 40 :
		print(" Well so you are a Young Man")
	elif x < 60 :		
		print(" Well so you are a Matured Man")
	else :
		print(" Well so you are a Senior")
