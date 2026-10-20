# Aprovado, reprovado ou recuperação:
# Receba a média de um aluno e diga se ele foi aprovado (média >= 7),
# reprovado (média < 5) ou está de recuperação (5 <= média < 7).

# 1. Receber a média do aluno
media = float(input("Digite a média do aluno: "))

# 2. Verificar a situação do aluno
if media >= 7:
    print("O aluno foi aprovado.")
elif media < 5:
    print("O aluno foi reprovado.")
else:
    print("O aluno está em recuperação.")

