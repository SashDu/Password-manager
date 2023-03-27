from exceptions import ExitException
from database import DataBase
from models import User


class Logic:
    def __init__(self):
        self._db = DataBase()

    def auth(self):
        while True:
            print('Введите ваш логин или exit для выхода: ')
            login = input('> ')
            if login == 'exit':
                raise ExitException
            print('Введите ваш пароль или exit для выхода: ')
            password = input('> ')
            if login == 'exit':
                raise ExitException
            user: User = self._db._get_user_by_login(login=login)
            if user is not None:
                if user.validate_password(password=password):
                    return True
            else:
                print('Неверный логин или пароль, попробуйте еще раз!')

    def create_user(self):
        username = input('Введите имя пользователя\n >')
        password = input('Введите пароль\n >')
        extra_info = input('Введите дополнительные данные\n >')
        pass2 = input('Введите пароль ещё раз\n >')
        if pass2 == password:
            return self._db.create_user(
                login=username,
                password=password,
                extra_info=extra_info
            )




