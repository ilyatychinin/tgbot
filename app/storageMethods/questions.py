def get_questions(self, user_id, test):
    return self.users[user_id]["questions"].get(test, [])

def add_question(self, user_id, test, question_text):
    if test not in self.users[user_id]["questions"]:
        self.users[user_id]["questions"][test] = []
    self.users[user_id]["questions"][test].append(question_text)
    self.save_data()  # Сохраняем изменения