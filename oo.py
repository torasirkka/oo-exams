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

    def ask_and_evaluate(self):
        """Function that prints question and evaluates the result."""

        answer = input(f"{self.question} ")
        return answer == self.correct_answer


class Exam:
    """Define Exam class"""

    def __init__(self, name):
        """Initialize exam"""
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def calc_score(self, lst):
        return sum(lst) / len(lst)

    def administer(self):
        """administer all questions in test & evaluate score."""

        lst = []
        for question in self.questions:
            if question.ask_and_evaluate():
                lst.append(1)
            else:
                lst.append(0)
        return self.calc_score(lst)


class Quiz(Exam):
    """Define Quiz class.

    This class behaves like it's super class 'Exam', with the exception that
    the administer-method should return 1 if the score is > 0.5 and false
    otherwise."""

    def __init__(self, name):
        super().__init__(name)

    def add_question(self, question):
        super().add_question(question)

    def calc_score(self, lst):
        return round(sum(lst) / len(lst))

    def administer(self):
        result = super().administer()
        return result


class StudentExam:
    """Class that stores a student and exam instance, administers the exam and stores the resulting score."""

    def __init__(self, student, exam):
        """Instantiate an exam for a student"""
        self.student = student
        self.exam = exam
        self.score = None

    def _print_score(self, score):
        print(f"Your score is: {score}.")

    def take_test(self):
        print(f"\nHi, {self.student.first_name}. Welcome to the {self.exam.name} exam!")
        print("*" * 40)
        print("")
        self.score = self.exam.administer()
        self._print_score(self.score)
        return self.score


class StudentQuiz(StudentExam):
    """Creating a student class."""

    def __init__(self, student, exam):
        super().__init__(student, exam)

    def print_score(self, score):
        print(f"Your quizz result is: {score}.")

    def take_test(self):
        self.score = super().take_test()


if __name__ == "__main__":

    # For examining Exam and Quiz- related classes:
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

    # Instantiate student 'Jasmine'
    Jasmine = Student("Jasmine", "Debugger", "0101 Computer Street")

    # Instantiate studentexam object,
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

    Jasmine = Student("Jasmine", "Debugger", "0101 Computer Street")

    studentquiz = StudentQuiz(Jasmine, quiz1)
    studentquiz.take_test()
