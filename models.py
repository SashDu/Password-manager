class Operations:
    def __init__(self):
        pass


class AddResource:
    def __init__(self):
        self.category = None
        self.id = None
        self.extra_info = None


class AddLogin:
    def __init__(self):
        self.id = None
        self.extra_info = None


class AddPassword:
    def __init__(self):
        self.id = None
        self.extra_info = None


class User:
    def __init__(self, user_id, name, password, extra_info):
        self._id = user_id
        self._name = name
        self._password = self.password_hash(password)
        self._extra_info = extra_info

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_pass):
        self._password = self.password_hash(new_pass)

    @property
    def extra_info(self):
        return self._extra_info

    @staticmethod
    def password_hash(password):
        return hash(password)

    def validate_password(self, password):
        if self._password == hash(password):
            return True
        return False

    def as_dict(self):
        return vars(self)





