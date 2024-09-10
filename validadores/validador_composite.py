from validador_base import Validador

class ValidadorComposite(Validador):
    def __init__(self):
        self._validadores = []

    def adicionar(self, validador):
        self._validadores.append(validador)

    def remover(self, validador):
        self._validadores.remove(validador)

    def validar(self, valor):
        return all(validador.validar(valor) for validador in self._validadores)
