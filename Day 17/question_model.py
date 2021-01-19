class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


question_1 = Question("Hola", "False")
print(question_1)