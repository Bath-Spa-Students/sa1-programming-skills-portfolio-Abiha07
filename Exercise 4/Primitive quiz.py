def analyse_answer(question, correct_answer):
    # display the question and get the answer
    answer = input(question + " ").strip()
   
    # analyse if the answer is correct, leave it if its wrong
    if answer.lower() == correct_answer.lower():
        print("Correct answer!")
    else:
        print("wrong answer!")

# quiz for 10 european country capital questions
questions = {
    "What do you think is the capital of France?": "Paris",
    "What do you think is the capital of Italy?": "Rome",
    "What do you think is the capital of Spain?": "Madrid",
    "What do you think is the capital of Germany?": "Berlin",
    "What do you think is the capital of Portugal?": "Lisbon",
    "What do you think is the capital of Netherlands?": "Amsterdam",
    "What do you think is the capital of Belgium?": "Brussels",
    "What do you think is the capital of Austria?": "Vienna",
    "What do you think is the capital of Switzerland?": "Bern",
    "What do you think is the capital of Greece?": "Athens",
}

# analyse through every question for correct answer
for question, correct_answer in questions.items():
    analyse_answer(question, correct_answer)
