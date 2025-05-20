# i want this program to ask the user for
#their name "What's your name?" and then,
# i want the program to say "Hi, NAME"
# then i want it to ask the user's age
# and make a comment on it

# step 1, ask the user what their name is
print("What is your name?")
# step 2: input the user's name from the keyboard
# and save it into a variable so we can use it later
user_name = input()
# step 3: say hi back using the user's name
print("Hi, " + user_name , ".")
# step 4: ask user for their age
print("How old are you? ")
# step 5: allow user to enter their age
user_age = input()
# step 6: add a response
print("Wow! " + user_age , "is old!")