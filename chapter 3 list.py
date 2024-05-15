#chapter 3 list
#
name_list = ["Mike","Paul","Zed"]

print("Happy Birthday!" + " " + name_list[0] + ".")
print("Happy Birthday!" + " " + name_list[1] + ".")
print("Happy Birthday!" + " " + name_list[2] + ".")
#invite list
invite_list = ["Mike","Paul","Zed"]
#Mike unable to provide
pop_invite_list = invite_list.pop(0)
print("Today invite"+ " "+ invite_list[0] + " and " + invite_list[1]+ " join us.")
print("Unable to show up is"+ " " + pop_invite_list)
#more people want to join
invite_list.append("Me")
invite_list.insert(2, "ILL")
invite_list.insert(0, "UNci")
print(invite_list)
#delete someone from list
invite_list.pop()
print(invite_list)
invite_list.pop()
print(invite_list)
invite_list.pop()
print(invite_list)

del invite_list[1]
del invite_list[0]
print(invite_list)

#Some place I want to go
favorite_place = ["London","Paris","New Tork","Japan","Taiwan"]
print(favorite_place)
favorite_place.sort()
print(favorite_place)
favorite_place.sort(reverse=True)
print(favorite_place)