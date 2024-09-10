from validadores.validador_tamanho import ValidadorTamanhoMinimo
from validadores.validador_caracteres import ValidadorCaracteresEspeciais
from validadores.validador_composite import ValidadorComposite

# Criando validadores individuais
validador_tamanho = ValidadorTamanhoMinimo(8)
validador_caracteres = ValidadorCaracteresEspeciais()

# Criando o composite e adicionando os validadores
validador_composite = ValidadorComposite()
validador_composite.adicionar(validador_tamanho)
validador_composite.adicionar(validador_caracteres)

# Testando o validador composite
senha = "Senha@123"
if validador_composite.validar(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")
