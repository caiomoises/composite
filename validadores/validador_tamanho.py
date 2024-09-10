from validador_base import validador

class ValidadorTamanhoMinimo(validador):
    def __init__(self, tamanho_minimo):
        self.tamanho_minimo = tamanho_minimo

    def validar(self, valor):
        return len(valor) >= self.tamanho_minimo
