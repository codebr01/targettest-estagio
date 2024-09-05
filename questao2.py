def verificarLetraA(string):
    string_minuscula = string.lower()

    return string_minuscula.count('a')

# Exemplo de uso
texto = input("Digite uma string: ")
contagem = verificarLetraA(texto)

if contagem > 0:
    print(f"A letra 'a' aparece {contagem} vezes.")
else:
    print("A letra 'a' não aparece na string.")