sum = 0
while(True):
	userInput = input("Enter the Price of the item or press q to quit: \n")
	if (userInput!='q'):
		sum = sum + float(userInput)
		print(f"order total so far: {sum}")

	else:
		print(f"Your Total Bill is = {sum}")
		print("Thanks For Using Our Calculator")
		break
