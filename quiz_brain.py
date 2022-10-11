


class QuestionBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.quest_list = question_list
        self.score = 0
    
    def next_question(self):
        current_question = self.quest_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number} :{current_question.text} (True/False) :")
        self.check_answer(user_answer, current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print(f"YOU GOT IT")
        else:
            print("SORRY FOR YOU")
        print(f"The Right answer is {correct_answer}")
        print(f"Your Score is {self.score}/{self.question_number}")
        print("\n")

        
    def still_has_question(self):
        if self.question_number < len(self.quest_list):

            return True
        else: 
             False

   



