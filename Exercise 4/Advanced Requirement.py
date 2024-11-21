# Add a dictionary storing countries with their capitals for the quiz
# The keys are country names, and the values are their capitals
quiz_format = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Switzerland": "Bern",
    "Greece": "Athens"
}

# value to keep track of the user's score
score = 0

# Loop through each country-capital pair in the quiz
for country, capital in quiz_format.items():
    # Ask the user for the capital of the current country
    user_answer = input(f"What is  the capital of {country}? ").strip() # .strip() Removes extra spaces around input

    # Check if the answer is correct, ignoring case differences
    if user_answer.lower() == capital.lower():
        # If correct, acknowledge and add to the score
        print("wow! That's correct.")
        score += 1
    else:
        # If incorrect,  provide the correct answer
        print(f"whoops, but the capital of {country} is  {capital}.")

# show the user's final score with encouragement
print(f"\nwell done! You scored {score} out of {len(quiz_format)}.")
