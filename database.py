import csv
from models import User
from utils import file_saver


class DataBase:
    def __init__(self):
        self._users: list[User] = list()
        self._users_login_index: dict[str, int] = dict()
        self._user_curr_id = 1
        self._user_id_generator = self._user_id_generator_func()
        self._fill_users_from_file()
        self._user_curr_id = self._users[-1].id

    def _fill_db_by_default(self):
        self.create_user(
            login='admin',
            password='admin',
            extra_info='Minsk'
        )

    def _get_user_by_id(self, user_id: int) -> [User, None]:
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def _get_user_by_login(self, login: str) -> [User, None]:
        for user in self._users:
            if user.name == login:
                return user
        return None

    def _user_id_generator_func(self):
        while True:
            yield self._user_curr_id
            self._user_curr_id += 1

    @file_saver
    def create_user(self, login: str, password: str, extra_info: str) -> bool:
        user = User(
            user_id=next(self._user_id_generator),
            name=login,
            password=password,
            extra_info=extra_info
        )
        self._users.append(user)
        self._users_login_index[login] = len(self._users)
        return user.id

    @file_saver
    def update_user(self, user_id: int, login: str = None, password: str = None, extra_info: str = None):
        user = self._get_user_by_id(user_id=user_id)
        if login is not None:
            user.name = login
        if password is not None:
            user.password = password
        if extra_info is not None:
            user.extra_info = extra_info
        return True

    @file_saver
    def delete_user(self, user_id: int = None, login: str = None):
        if user_id is None and login is None:
            return False

        if login is not None:
            pos = self._users_login_index.get(login)
            user = self._users[pos]
            if user.id == user_id:
                self._users[pos] = dict()
                del self._users_login_index[login]
                return True
        i = 0
        while i < len(self._users):
            if self._users[i].id == user_id:
                if login is not None and self._users[i].name == login:
                    del self._users[i]
                    return True
        return False

    def _fill_users_from_file(self):
        try:
            with open('database.user.csv', 'r') as file:
                csv_reader = csv.DictReader(f=file, delimiter='|')
                for row in csv_reader:
                    self._users.append(row)
        except FileNotFoundError:
            self._fill_db_by_default()