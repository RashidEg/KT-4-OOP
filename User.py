class User:
    # Счетчик для обычных пользователей
    count = 0

    def __init__(self, name: str, login: str, password: str, grade: int):
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade
    # Увеличиваем счетчик при создании нового пользователя этого класса
        if type(self) is User:
            User.count += 1

    # Свойства для name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    # Свойства login
    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value: str):
        print("Невозможно изменить логин!")
    # Свойства password
    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value: str):
        self._password = value

    # Свойства grade
    @property
    def grade(self):
        return "Неизвестное свойство grade"

    @grade.setter
    def grade(self, value: int):
        print("Неизвестное свойство grade")

    # Методы 
    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}")

    def __eq__(self, other):
        if isinstance(other, User):
            return self._grade == other._grade
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, User):
            return self._grade < other._grade
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, User):
            return self._grade > other._grade
        return NotImplemented


class SuperUser(User):
    # Отдельный счетчик для супер-пользователей
    count = 0

    def __init__(self, name: str, login: str, password: str, role: str, grade: int):
        super().__init__(name, login, password, grade)
        self._role = role
        # Увеличиваем счетчик при создании нового супер-пользователя
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value: str):
        self._role = value

    def show_info(self):
        print(f"Name: {self._name}, Login: {self._login}, Role: {self._role}")

# Проверка
if __name__ == '__main__':
    user1 = User('Paul McCartney', 'paul', '1234', 3)
    user2 = User('George Harrison', 'george', '5678', 2)
    user3 = User('Richard Starkey', 'ringo', '8523', 3)
    admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

    user1.show_info()
    admin.show_info()

    users = User.count
    admins = SuperUser.count
    print(f'Всего обычных пользователей: {users}')
    print(f'Всего супер-пользователей: {admins}')

    print(user1 < user2)
    print(admin > user3)
    print(user1 == user3)

    user3.name = 'Ringo Starr'
    user1.password = 'Pa$$w0rd'

    print(user3.name)
    print(user2.password)
    print(user2.login)

    user2.login = 'geo'
    print(user1.grade)
    admin.grade = 10