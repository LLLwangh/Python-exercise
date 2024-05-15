#chapter 5 of peration

car = 'amd'
if car == 'subaru':
    print("Is car subaru? I predict True")
    print(car.lupper() + " is True.")
else:
    print("Is car subaru? I predict False")
    print(car.lower() + " is False.")

#alien color
gain = 0
colors =["green","red","yellow"]
if "green" in colors:
    gain = gain + 5
    print("Player gain 5 points from green alien")
if "red" in colors:
    gain = gain + 3
    print("Player gain 3 points from red alien")
if "yellow" in colors:
    gain = gain + 1
    print("Player gain 1 points from yellow alien")
else:
    print("you missed")
print(gain)
#age
age = 61
if age < 2:
    print("He is an Infant")
elif age >= 2 and age <4:
    print("He is learning how to walk")
elif age >= 4 and age <13:
    print("He is a baby")
elif age >= 13 and age <20:
    print("He is a teenage")
elif age >= 20 and age <62:
    print("He is an adult")
else:
    print("He is an old man")

# say hello
old_users = ["Mateo Pena","Vanessa Beard","Charles Vasquez","Arjun Wright","Effie John"]
new_users = ["Mateo Pena","Sid Keith","Aaron Noble","Amelie Golden","Poppie Robles"]

for new_user in new_users:
    if new_user in old_users:
        print(new_user + ". Sorry,name has been used")
    else:
        print(new_user + ", This name is avaible.")