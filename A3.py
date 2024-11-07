#Take input from user

math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
spanish = int(input("Spanish: "))

#work out percentage

total = math + english + science + spanish
perc = (total/400)*100

#Announcing Score
print(end = "The total percentage = ")
print(perc)
