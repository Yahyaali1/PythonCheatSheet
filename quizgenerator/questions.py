"""
To hold information for the Question
"""


class Question:

    def __init__(self, question_text="", answer_text=""):
        self.question = question_text
        self.answer_text = answer_text

    def validate_answer(self, answer_to_check=""):
        return self.answer_text == answer_to_check

