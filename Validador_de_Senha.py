def validar_senha(senha):

    tem_numero = False
    tem_maiuscula = False
    tem_minuscula = False

    # 1. Verifica o tamanho da senha
    if len(senha) < 8:
        print("Erro: A senha precisa ter pelo menos 8 caracteres.")
        return False

    # 2. Percorre a senha para verificar os critérios usando funções embutidas
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isupper():
            tem_maiuscula = True

    # 3. Verifica se todos os critérios foram atendidos de forma concisa
    if not tem_numero:
        print("Erro: A senha precisa ter pelo menos um número.")
        return False
    if not tem_minuscula:
        print("Erro: A senha precisa ter pelo menos uma letra minúscula.")
        return False
    if not tem_maiuscula:
        print("Erro: A senha precisa ter pelo menos uma letra maiúscula.")
        return False

    return True

# -----------PROGRAMA PRINCIPAL-----------

print("A senha precisa ter pelo menos 8 dígitos, contendo pelo menos um número, uma letra maiúscula e uma minúscula.")

# Usa um loop 'while' para pedir a senha até que seja válida
while True:
    senha_usuario = input("Digite a senha: ")

    if validar_senha(senha_usuario):
        print("Senha válida! Acesso concedido.")
        break
