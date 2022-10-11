from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain

question_array = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_array.append(new_question)

quiz = QuestionBrain(question_array)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz GOOD : )")
print(f"Your Final score is  {quiz.score}/{quiz.question_number}")




