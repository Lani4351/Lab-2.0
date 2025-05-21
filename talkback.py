# i want this program to ask the user for
#their name "What's your name?" and then,
# i want the program to say "Hi, NAME"
# then i want it to ask the user's birth year and subtract it from the current year
# to calulate the user's age and respond with how old they are

# step 1, ask the user what their name is
print("What is your name?")
# step 2: input the user's name from the keyboard
# and save it into a variable so we can use it later
user_name = input()
# step 3: say hi back using the user's name
print("Hi, " + user_name , ".")
# step 4: ask user for their age
print("What year were you born?")
# step 5: allow user to enter their birth year
user_birthyear = input()
# step 6: subtract birth year from current year
# print final answer with response to user's age
print("Wow! So that means you are about "
      + str(2025 - int(user_birthyear)) + " years old!")
