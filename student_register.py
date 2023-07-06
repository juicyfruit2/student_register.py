# A program that allows students to register for an exam venue.

# used build in function open to write out code 
f = open("Register.txt", "w")

# created a variable to ask the user a question 
user_input = int(input("How many students are registering ? :"))

# used for a loop to loop through the amount of students 
for ID in range (0,user_input):
    ID =  input( "Enter their ID Number:")
    f.write(ID + "\n")

f.close()