# Quiz App

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": [
            "A. Dennis Ritchie",
            "B. James Gosling",
            "C. Guido van Rossum",
            "D. Bjarne Stroustrup"
        ],
        "answer": "C"
    },
    {
        "question": "What is 5 × 6?",
        "options": ["A. 11", "B. 25", "C. 30", "D. 35"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    }
]

score = 0

print("=== Welcome to the Quiz App ===\n")

for i, q in enumerate(questions, start=1):
    print(f"Q{i}. {q['question']}")

    for option in q["options"]:
        print(option)

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {q['answer']}\n")

# Final Results
print("=== Quiz Finished ===")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good job!")
else:
    print("Keep practicing!")