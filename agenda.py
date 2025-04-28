from contato import Contato
from evento import Evento

class Agenda:
    _contatos = []
    _eventos = []

    @classmethod
    def contatos(cls):
        return cls._contatos

    @classmethod
    def eventos(cls):
        return cls._eventos

    def __init__(self, contato=None, evento=None):
        if contato:
            self._contatos.append(contato)
        if evento:
            self._eventos.append(evento)
