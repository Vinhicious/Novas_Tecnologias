from datetime import date

class Contato:
    __slots__ = ("_nome", "_telefone", "_datanasc", "_email")

    def __init__(self, nome=None, telefone=None, datanasc=None, email=None):
        self._nome = nome
        self._telefone = telefone
        self._datanasc = datanasc
        self._email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @property
    def datanasc(self):
        return self._datanasc

    @datanasc.setter
    def datanasc(self, valor):
        self._datanasc = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    def __str__(self):
        return f"{self._nome}\n{self._telefone}\n{self._datanasc.strftime('%d/%m/%Y')}\n{self._email}"
