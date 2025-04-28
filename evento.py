from datetime import date
from contato import Contato

class Evento:
    _total_eventos = 0

    def __init__(self, descricao, data_inicio, data_fim, contato):
        self._descricao = descricao
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._contato = contato
        Evento._total_eventos += 1

    def get_informacoes(self):
        return "Descrição: {0}\n{1} - {2}\nContato: {3}".format(
            self._descricao,
            self._data_inicio.strftime("%d/%m/%Y"),  
            self._data_fim.strftime("%d/%m/%Y"),
            self._contato._nome  
        )


    @staticmethod
    def get_total_eventos():
        return Evento._total_eventos
