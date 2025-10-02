class QuizBrain():
    def __init__(self, q_list = list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

# TODO: Method for asking the question
    def next_question(self):
        # current_question will hold a Question object
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

# TODO: Method for checking if answer correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the answer right!")
            self.score += 1
        else:
            print("That's wrong mate.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")


# TODO: checking if we are at the end of the quiz
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        return False