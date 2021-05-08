class Student:
    """Define Student class.

    Each student has a first_name, last_name and address."""

    def __init__(self, first_name, last_name, address):
        """Initialize student."""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question:
    """Dataclass for questions and answers."""

    def __init__(self, question, correct_answer=""):
        """Instantiate a question."""
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self) -> bool:
        """Function that prints question, reads and evaluates results. Returns a boolean
        if the answer is correct."""

        answer = input(f"{self.question} ")
        return answer == self.correct_answer


class Exam:
    """Define Exam class"""

    def __init__(self, name):
        """Initialize exam"""
        self.name = name
        self.questions = []

    def add_question(self, question: Question):
        """Modifies the exam instance attribute 'questions' of type list, by appending a
        question to it."""

        self.questions.append(question)

    def _calc_score(self, lst) -> float:
        """Calculates the score of the exam.

        The list lst must contain a list with zeros and ones representing incorrect and
        correct answers."""

        return sum(lst) / len(lst)

    def administer(self) -> float:
        """Administer all questions in test & evaluate score."""

        # For each answer: append 0 for incorrect answer, or one for a correct one.
        lst = []
        for question in self.questions:
            if question.ask_and_evaluate():
                lst.append(1)
            else:
                lst.append(0)
        return self._calc_score(lst)


class Quiz(Exam):
    """Define Quiz class.

    This class behaves like it's super class 'Exam', with the exception that
    the score is calculated in a different way. It is 1 if the the ratio correct
    to incorrect answers is >= 0.5, and 0 otherwise."""

    def __init__(self, name):
        super().__init__(name)

    def add_question(self, question):
        super().add_question(question)

    # _calc_score determines what's returned by administer(). Here we use round()
    # to return 1 when more than half the questions are correct and 0 otherwise.
    def _calc_score(self, lst):
        return round(sum(lst) / len(lst))

    def administer(self):
        result = super().administer()
        return result


class StudentExam:
    """Class that stores a student and exam instance, administers the exam and
    stores the resulting score."""

    def __init__(self, student, exam):
        """Instantiate an exam for a student"""
        self.student = student
        self.exam = exam
        self.score = None

    def _print_score(self, score):
        """Print the score"""
        print(f"Your score is: {score}.")

    def take_test(self):
        """Administer exam to student. Register result as instance attribute."""
        print(
            f"\nHi, {self.student.first_name}. Welcome to the {self.exam.name} examination!"
        )
        print("*" * 40)
        print("")
        self.score = self.exam.administer()
        self._print_score(self.score)
        return self.score


class StudentQuiz(StudentExam):
    """Creating a student class."""

    def __init__(self, student, exam):
        """Instantiate studentquiz object."""
        super().__init__(student, exam)

    def print_score(self, score):
        """Print the score"""
        print(f"Your quizz result is: {score}.")

    def take_test(self):
        """Administer the quiz to student. Register result as instance attribute."""
        self.score = super().take_test()


if __name__ == "__main__":

    # For examining Exam and Quiz- related classes:

    # Instantiate Student object 'Jasmine'
    Jasmine = Student("Jasmine", "Debugger", "0101 Computer Street")

    # Create question objects
    alberta_capital = Question("What is the capital of Alberta?", "Edmonton")
    python_author = Question("Who is the author of Python?", "Guido Van Rossum")
    set_q = Question("What is the method for adding and element to a set?", ".add()")

    # --------------------------------------------------------------
    # Create instance of exam
    midterm = Exam("Midterm")

    # Add questions to exam instance object 'midterm'
    midterm.add_question(alberta_capital)
    midterm.add_question(python_author)
    midterm.add_question(set_q)

    # Instantiate studentexam object
    studentexam = StudentExam(Jasmine, midterm)
    studentexam.take_test()

    # ---------------------------------------------------------------

    # Create exam 'Quiz'
    quiz1 = Quiz("Quiz")

    # Create question objects
    alberta_capital = Question("What is the capital of Alberta?", "Edmonton")
    python_author = Question("Who is the author of Python?", "Guido Van Rossum")
    set_q = Question("What is the method for adding and element to a set?", ".add()")

    # Add questions to Midterm exam
    quiz1.add_question(alberta_capital)
    quiz1.add_question(python_author)
    quiz1.add_question(set_q)

    # Instantiate studentquiz object
    studentquiz = StudentQuiz(Jasmine, quiz1)
    studentquiz.take_test()
