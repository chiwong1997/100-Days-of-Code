import question_model
from data import question_data
import quiz_brain

question_bank = []

# Each question object has a text attribute and a answer attribute 

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_q = question_model.Question(text=question_text, answer=question_answer)
    question_bank.append(new_q)

# The question_bank is a list of Question objects
# This list is fed into the QuizBrain object and will be an the value of the question_list 
# attribute for the QuizBrain object
print(question_bank)
# We can access the text and answer attribute 
# for each Question object in the question_bank list
print(question_bank[2].text)

# REMEMBER:
# quiz is the object 
# quiz_brain is the module imported
# QuizBrain is the class
quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was {quiz.score}. Congratulations!")