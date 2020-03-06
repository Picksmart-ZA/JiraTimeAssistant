class Settings:
    __url = ""
    __user = ""
    __password = ""

    def __init__(self, __url, __user, __password):
        self.__url = __url
        self.__user = __user
        self.__password = __password

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password
