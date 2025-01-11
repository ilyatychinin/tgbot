def get_disciplines(self, user_id):
    return self.users[user_id]["disciplines"]

def add_discipline(self, user_id, discipline_name):
    self.users[user_id]["disciplines"].append(discipline_name)
    self.save_data()  # Сохраняем изменения

# Методы для работы с текущей дисциплиной
def set_current_discipline(self, user_id, discipline):
    self.users[user_id]["current_discipline"] = discipline
    self.save_data()  # Сохраняем изменения

def get_current_discipline(self, user_id):
    return self.users[user_id]["current_discipline"]