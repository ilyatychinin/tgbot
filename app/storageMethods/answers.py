def set_answer_count(self, user_id, count):
    self.users[user_id]["answer_count"] = count
    self.save_data()  # Сохраняем изменения

def get_answer_count(self, user_id):
    return self.users[user_id]["answer_count"]

def set_answers(self, user_id, answers):
    self.users[user_id]["answers"] = answers
    self.save_data()  # Сохраняем изменения

def get_answers_for_question(self, user_id, question):
    """Возвращает список ответов для заданного вопроса."""
    return self.users[user_id]["questions"].get(question, {}).get("answers", [])

def get_answers(self, user_id):
    return self.users[user_id]["answers"]

def set_correct_answer(self, user_id, correct_answer):
    self.users[user_id]["correct_answer"] = correct_answer
    self.save_data()  # Сохраняем изменения

def get_correct_answer(self, user_id):
    return self.users[user_id]["correct_answer"]