class Checker:
    def __init__(self, data):
        self.data = data

    def check(self):
        pass


class CheckerLogin(Checker):
    def __init__(self, data):
        self.data = data[0]
        self.passw = data[1]

    def check(self):
        if len(self.data) <= 3:
            return 'Недостаточная длина логина'
        else:
            check_pass = CheckerPassword(self.passw)
            result_pass = check_pass.check()
            return result_pass


class CheckerPassword(Checker):
    def __init__(self, data):
        self.data = data

    def check(self):
        if len(self.data) < 8:
            return 'Недостаточная длина пароля'
        elif self.data.isdigit() or self.data.isalpha():
            return 'В пароле должны быть и цифры, и буквы'
        elif self.data.islower() or self.data.isupper():
            return 'В пароле должны быть и строчные, и прописные буквы'
        else:
            return 'OK'