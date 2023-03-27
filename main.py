from services import Logic


class PasswordManger:
    def __init__(self):
        self._authorization = Logic()

    def start(self):
        if self._authorization.auth():
            print(self._logic.create_user())
        else:
            print('Аутентификация не успешна')


if __name__ == '__main__':
    manager = PasswordManger()
    manager.start()

