#simple message

#Pratice for python return print function and output message
message = "Hello world"
print(message)
msg = "Hello python's user!."
print(msg)

#string
'This is a string'
"This is also a string"

#Print first charactor of name as Capital letter
name = "Ada smith"
print(name.title())

#combine two string with one space
first_name = "ada"
last_name = "smith"
full_name = first_name +" "+ last_name
print(full_name)

#to change row and tap first column with \n and \t
print("language:\nPython\nC++\nJava")
print("language:\n\tPython\n\tC++\n\tJava")

#delete space
language = '   Java+++  '
print(language.rstrip())
print(language.lstrip())
print(language.strip())

#name
user_name = "mike chan"
print("Hello" + " "+ user_name.title()+ "," +"How are you?")
print("Hello" + " "+ user_name.upper()+ "," +"How are you?")
print("Hello" + " "+ user_name.lower()+ "," +"How are you?")

#number
print(5 + 3)