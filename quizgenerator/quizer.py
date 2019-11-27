"""
To fetch questions and answer out of given file.
To pose quiz
"""

from questions import Question
import random


class Quizzer:

    def __init__(self, ques_file_name="", ans_file_name=""):

        question_file = open(ques_file_name)
        ans_file = open(ans_file_name)

        questions = question_file.readlines()
        answers = ans_file.readlines()

        self.__questions = [Question(self.__remove_key_text(questions[i]), self.__remove_key_text(answers[i]))
                            for i in range(len(questions))]

        question_file.close()
        ans_file.close()

    def __remove_key_text(self, item=""):
        item = item.split(".", 1)[-1]
        return item.strip()

    def __randomize_questions(self):
        random.shuffle(self.__questions)
        pass

    def start_quiz(self):
        user_results = []
        self.__randomize_questions()
        print("Here is the list of Questions")

        for i in range(len(self.__questions)):
            print(f'Q{i+1} - {self.__questions[i].fetch_question()} \n')

        print("Now Give Answers")
        for i in range(len(self.__questions)):
            print(f'Answer {i+1} - :')
            user_results.append(self.__questions[i].validate_answer(input()))

        print("Now Your Results")
        for i in range(len(user_results)):
            print(f'Your ans was correct for question{i+1}' if user_results[i]
                  else f'Wrong answer, correct ans is {self.__questions[i].fetch_answer()}')




