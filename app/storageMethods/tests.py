def get_tests(self, user_id, discipline):
    return self.users[user_id]["tests"].get(discipline, [])

def add_test(self, user_id, discipline, test_name):
    if discipline not in self.users[user_id]["tests"]:
        self.users[user_id]["tests"][discipline] = []
    self.users[user_id]["tests"][discipline].append(test_name)
    self.save_data()  # Сохраняем изменения

    # Методы для работы с текущим тестом
def set_current_test(self, user_id, test):
    self.users[user_id]["current_test"] = test
    self.save_data()  # Сохраняем изменения

def get_current_test(self, user_id): 
    return self.users[user_id]["current_test"]

def clear_tests(self, user_id):
    print(f" Очистка тестов для пользователя {user_id}...")
    if user_id in self.users:
        self.users[user_id]["tests"] = {}
        self.save_data()  # Сохраняем изменения
        print(f"Тесты для пользователя {user_id} очищены.")