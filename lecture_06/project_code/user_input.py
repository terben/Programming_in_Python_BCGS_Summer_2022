# As we discussed in class, user input should be handled via command-line
# arguments rather than with direct interaction if possible.
#
# For cases such as the physics718 word-game, we need interactive user-input
# of course. This file shows the essentials.

# Ask the user for an input from the keyowrd (the input-command):

user_input = input("Please give me some input: ")

# The type of the ionput is a string:
print(type(user_input), user_input)

# The following construct might be useful if you want to
# avoid errorneous empty input:

# If the user just presses enter after the input-query, we
# just repeat the query before continuing:

user_input = ""
while user_input == "":
      user_input = input("Please give me some input: ")

print(user_input)
