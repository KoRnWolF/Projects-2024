class QuizBrain:
    def __init__(self, question_l):
        self.question_number = 0
        self.question_list = question_l
        self.score = 0

    def still_has_question(self):
        """Method : checks if all questions have been asked from list"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Method : increases question number and prints/inputs new question"""
        new_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {new_q.text} Is this statement (True or False)?\n").capitalize()
        self.check_answer(user_answer, new_q.answer)

    def check_answer(self, usr_ans, correct_a):
        """Method : Check user answer against list answer"""
        if usr_ans == correct_a:
            print("Correct!")
            self.score += 1
            print(f"Your score : {self.score}/{len(self.question_list)}")
        else:
            print("Incorrect!")
            print(f"Your score : {self.score}/{len(self.question_list)}")

        print(f"The correct answer is : {correct_a}\n")