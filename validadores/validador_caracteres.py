from validador_base import Validador

class ValidadorCaracteresEspeciais(Validador):
    def validar(self, valor):
        caracteres_especiais = "!@#$%^&*()-+"
        return any(c in caracteres_especiais for c in valor)