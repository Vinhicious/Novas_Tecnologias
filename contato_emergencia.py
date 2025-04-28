from agenda import Contato

class ContatoEmergencia(Contato):
    def __init__(self, nome, telefone, datanasc, email, prioridade=True):
        super().__init__(nome, telefone, datanasc, email)
        self._prior = prioridade

    @property
    def prioridade(self):
        return self._prioridade

    @prioridade.setter
    def prioridade(self,prior):
        self._prior = prioridade
