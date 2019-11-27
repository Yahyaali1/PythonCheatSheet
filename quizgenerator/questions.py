"""
To hold information for the Question
"""


class Question:

    def __init__(self, question_text="", answer_text=""):
        self.__question = question_text
        self.__answer_text = answer_text

    def fetch_question(self):
        return self.__question

    def fetch_answer(self):
        return self.__answer_text

    def validate_answer(self, answer_to_check=""):
        return self.__answer_text == answer_to_check

