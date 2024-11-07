#Taking input from the user

amount = int(input("State the amount of money you would like to withdraw. "))

#calculatingStuff
note1 = amount//50 
note2 = (amount%50)//10
note3 = ((amount%50)%10)//5

#INFO FOR CUSTOMER

print("Amount of £50 notes:  ", note1)
print("Amount of £10 notes:  ", note2)
print("Amount of £5 notes:  ", note3)