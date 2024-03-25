# from filename import variables
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

qb = QuizBrain(question_bank)


def show_question():
    currentScore = 0

    while True:
        question = qb.question_list[qb.question_number].text
        answer = qb.question_list[qb.question_number].answer
        ans = str(input(question + " True/False ?"))
        question_number = qb.question_number + 1
        if ans == answer:
            currentScore += 1
            print(
                f"You got it right!\nThe correct answer was:{answer}\nYour current score is: {currentScore}/{question_number}"
            )
        elif not bool(ans) == bool(answer):
            print(
                f"You got it wrong\nThe correct answer was:{answer}\nYour current score is: {currentScore}/{question_number}"
            )
        qb.next_question()


show_question()
