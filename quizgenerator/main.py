from quizer import Quizzer


def main():
    quizzer = Quizzer("questions.txt", "key.txt")
    quizzer.start_quiz()

main()
