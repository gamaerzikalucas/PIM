import os
import re

# Arquivos
USUARIOS = "usuarios.txt"
RESPOSTAS = "respostas_quiz.txt"

# Validação de senha forte
def validar_senha(senha):
    return (
        len(senha) >= 8 and
        re.search(r"[A-Z]", senha) and
        re.search(r"[a-z]", senha) and
        re.search(r"[0-9]", senha) and
        re.search(r"[\W_]", senha)
    )

# Criação de senha
def criar_senha():
    print("\n=== CRIAR SENHA SEGURA ===")
    nome = input("Digite seu nome: ")
    while True:
        senha = input("Crie uma senha (mín. 8 caracteres, com maiúscula, minúscula, número e símbolo): ")
        if validar_senha(senha):
            with open(USUARIOS, "a") as f:
                f.write(f"{nome},{senha}\n")
            print("Senha criada com sucesso!\n")
            break
        else:
            print("Senha fraca! Tente novamente.")

# Simulador de login
def simulador_login():
    print("\n=== SIMULADOR DE LOGIN ===")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")
    with open(USUARIOS, "r") as f:
        for linha in f:
            usuario, senha_armazenada = linha.strip().split(",")
            if nome == usuario and senha == senha_armazenada:
                print("Login bem-sucedido!\n")
                return True
    print("Seu cadastro está inválido! (tente colocar seu nome de forma legível, e crie uma senha mais forte).\n")
    return False

# Quiz final
def quiz():
    print("\n=== QUIZ FINAL ===")
    nome = input("Digite seu nome para iniciar o quiz: ").strip()

    perguntas = [
        {
            "numero": 1,
            "texto": "O que é um site falso (phishing)?\n"
                     "a) Um site de jogos\n"
                     "b) Um site que imita outro para roubar dados\n"
                     "c) Um blog de receitas\n> ",
            "correta": "b",
            "explicacao": "Phishing é um golpe que utiliza sites falsos para enganar as pessoas e roubar dados como senhas e informações bancárias."
        },
        {
            "numero": 2,
            "texto": "Qual dessas senhas é mais segura?\n"
                     "a) Abc@1234\n"
                     "b) 123456\n"
                     "c) senha123\n> ",
            "correta": "a",
            "explicacao": "Senhas seguras misturam letras maiúsculas e minúsculas, números e símbolos. 'Abc@1234' é a única que atende a esses critérios."
        },
        {
            "numero": 3,
            "texto": "O que você deve fazer ao receber um link suspeito?\n"
                     "a) Clicar sem pensar\n"
                     "b) Compartilhar com amigos\n"
                     "c) Verificar antes de clicar\n> ",
            "correta": "c",
            "explicacao": "Nunca clique diretamente em links suspeitos. Verifique a fonte antes para evitar golpes ou infecções por vírus."
        },
        {
            "numero": 4,
            "texto": "O que é um algoritmo?\n"
                     "a) Um tipo de vírus de computador\n"
                     "b) Um conjunto de passos para resolver um problema\n"
                     "c) Um programa de TV\n> ",
            "correta": "b",
            "explicacao": "Algoritmo é uma sequência lógica de instruções usada para resolver problemas ou realizar tarefas específicas."
        },
        {
            "numero": 5,
            "texto": "Qual é o principal direito garantido pela LGPD?\n"
                     "a) O direito de vender dados\n"
                     "b) O direito de ser pago pela internet\n"
                     "c) O direito à privacidade e controle dos dados pessoais\n> ",
            "correta": "c",
            "explicacao": "A LGPD garante ao cidadão o controle sobre seus dados pessoais, promovendo o direito à privacidade e segurança das informações."
        },
        {
            "numero": 6,
            "texto": "Qual atitude é considerada ética no uso da internet?\n"
                     "a) Espalhar informações falsas\n"
                     "b) Compartilhar dados sem permissão\n"
                     "c) Respeitar a privacidade e a opinião dos outros\n> ",
            "correta": "c",
            "explicacao": "A ética digital envolve o respeito à privacidade, à opinião dos outros e o combate à desinformação."
        },
        {
            "numero": 7,
            "texto": "O que significa pensar logicamente em programação?\n"
                     "a) Acreditar que tudo é possível\n"
                     "b) Seguir passos claros para chegar a um resultado\n"
                     "c) Ignorar erros e continuar\n> ",
            "correta": "b",
            "explicacao": "Pensar logicamente é seguir uma sequência de passos organizados e coerentes para resolver problemas ou criar programas."
        },
        {
            "numero": 8,
            "texto": "Qual dessas ações desrespeita os direitos humanos na internet?\n"
                     "a) Ajudar alguém com dificuldade\n"
                     "b) Discriminar pessoas online\n"
                     "c) Criar conteúdos educativos\n> ",
            "correta": "b",
            "explicacao": "Discriminar pessoas online é uma violação dos direitos humanos. Respeito e empatia são fundamentais também no ambiente digital."
        }
    ]

    pontuacao = 0
    respostas_usuario = []

    with open(RESPOSTAS, "a") as resp_file:
        for pergunta in perguntas:
            while True:
                resposta = input(pergunta["texto"]).strip().lower()
                if resposta in ['a', 'b', 'c']:
                    break
                else:
                    print("Resposta inválida. Escolha a, b ou c.")
            respostas_usuario.append((pergunta, resposta))
            resp_file.write(f"{nome}, Pergunta {pergunta['numero']}: {resposta}\n")

    print("\n=== RESULTADO DO QUIZ ===")

    for pergunta, resposta in respostas_usuario:
        if resposta == pergunta["correta"]:
            pontuacao += 1
        else:
            print(f"\n❌ Pergunta {pergunta['numero']} incorreta:")
            print(pergunta["texto"].split("\n")[0])  # Apenas o enunciado
            print(f"✔ Resposta correta: {pergunta['correta']}")
            print(f"ℹ Explicação: {pergunta['explicacao']}")

    print(f"\n✅ Você acertou {pontuacao}/8.")

    if pontuacao >= 6:
        print(f"Parabéns, {nome}! Você teve um bom desempenho.")
    else:
        print(f"{nome}, tente novamente para melhorar sua pontuação.")

# Módulo de aprendizado extra sobre segurança digital
def aprender_mais():
    print("\n=== APRENDIZADO EXTRA: SEGURANÇA DIGITAL ===")

    perguntas_extras = [
        {
            "pergunta": "Por que é importante usar uma conexão segura (HTTPS)?",
            "resposta": "O HTTPS garante que a conexão entre seu navegador e o site seja criptografada, protegendo seus dados contra interceptações.",
        },
        {
            "pergunta": "O que é um golpe de engenharia social?",
            "resposta": "É quando um golpista manipula alguém para obter informações confidenciais, como senhas ou números de cartão, se passando por uma pessoa confiável.",
        }
    ]

    for p in perguntas_extras:
        input(f"\n👉 {p['pergunta']}\n(Aperte Enter para ver a explicação)")
        print(f"💡 {p['resposta']}")

    print("\n✅ Obrigado por aprender mais sobre segurança digital!\n")

# Menu principal
def menu():
    while True:
        print("\n=== SISTEMA DE NAVEGAÇÃO SEGURA ===")
        print("1 - Criar senha segura")
        print("2 - Simular login")
        print("3 - Fazer quiz final")
        print("4 - Aprender mais sobre segurança digital")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_senha()
        elif escolha == "2":
            simulador_login()
        elif escolha == "3":
            quiz()
        elif escolha == "4":
            aprender_mais()
        elif escolha == "5":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar
if __name__ == "__main__":
    for arquivo in [USUARIOS, RESPOSTAS,]:
        if not os.path.exists(arquivo):
            with open(arquivo, "w"): pass
    menu()
