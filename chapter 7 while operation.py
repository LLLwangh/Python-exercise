#chpater 7 while operation

car = input("Which make of car do you want most? : ")
print("Let me see if I can find you a " + str(car))

guest = input("How many guest will be presented tonight: ")
if int(guest) >= 8:
    print("Sorry, we have no table for " + str(guest) + " people.")
else:
    print("Yes, We have empty table for " + str(guest) + " people.")

finished_sandwich = {}
sandwich_ordering = {"Caprese Sandwich", "Club Sandwich", "Mediterranean Veggie Sandwich"}

for sandwich in sandwich_ordering:
    print("I will make you " + sandwich + ".")
    # Assuming the sandwich is made here and stored in a variable called "made_sandwich"
    finished_sandwich[sandwich] = "ready"

print("Finished sandwiches:", finished_sandwich)

