
# Solicitar o número de alunos a serem cadastrados
num_alunos = int(input("Digite o número de alunos a serem cadastrados: "))

# Lista para armazenar os dados dos alunos
turma = []

# Loop para cadastrar cada aluno
for i in range(num_alunos):
    print(f"\n--- Aluno {i + 1} ---")
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota (0-10): "))
    nota2 = float(input("Digite a segunda nota (0-10): "))
    nota3 = float(input("Digite a terceira nota (0-10): "))

    # Calcular a média
    media = (nota1 + nota2 + nota3) / 3

    # Determinar a situação
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0 and media < 7.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Armazenar os dados do aluno
    aluno = {
        "nome": nome,
        "notas": [nota1, nota2, nota3],
        "media": media,
        "situacao": situacao
    }
    turma.append(aluno)

# Exibir o boletim da turma
print("\n--- Boletim da Turma ---")
for aluno in turma:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")
    print("-" * 30)