# Ask the user to name the capital of France, ignoring any extra spaces
user_answer = input("what do you think is the capital of France? ").strip() # .strip() Removes extra spaces around input

# analyse if the answer is correct, ignoring case differences
if user_answer.lower() == "paris":
    # Let the user know they got it right
    print("That's right! Paris is the capital of france.")
else:
    # politely let the user know the answer is incorrect
    print("Whoops! The correct answer is Paris.")