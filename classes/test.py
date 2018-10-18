class PubliCup:
    def __init__(self):
        self.color = None
        self.content = None

    def fill(self, bevrage):
        self.content = bevrage

    def empty(self):
        self.content = None


class ProtectedCup:
    def __init__(self):
        self.color = None
        self._content = None

    def fill(self, bevrage):
        self._content = bevrage

    def empty(self):
        self._content = None


class PrivateCup:
    def __init__(self):
        self.color = None
        self.__content = None

    def fill(self, bevrage):
        self.__content = bevrage

    def empty(self):
        self.__content = None
