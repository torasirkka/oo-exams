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

    questions = []

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        """administer all questions in test & evaluate score."""

        lst = []
        for question in self.questions:
            if question.ask_and_evaluate():
                lst.append(1)
            else:
                lst.append(0)
        return sum(lst) / len(lst)


class StudentExam:
    """Class that stores a student and exam instance, administers the exam and stores the resulting score."""

    def __init__(self, student, exam):
        """Instantiate an exam for a student"""
        self.student = student
        self.exam = exam

    def take_test(self):
        print(f"\nHi, {self.student.first_name}. Welcome to the {self.exam.name} exam!")
        print("*" * 40)
        print("")
        score = self.exam.administer()
        print(f"Your score is: {score}.")


if __name__ == "__main__":

    # Create exam 'Midterm'
    midterm = Exam("Midterm")

    # Create question objects
    alberta_capital = Question("What is the capital of Alberta?", "Edmonton")
    python_author = Question("Who is the author of Python?", "Guido Van Rossum")
    set_q = Question("What is the method for adding and element to a set?", ".add()")
    # Add questions to Midterm exam
    midterm.add_question(alberta_capital)
    midterm.add_question(python_author)
    midterm.add_question(set_q)

    Jasmine = Student("Jasmine", "Debugger", "0101 Computer Street")

    studentexam = StudentExam(Jasmine, midterm)
    studentexam.take_test()
