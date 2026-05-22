idade=18
nota=9
frequencia=75

if idade >= 18 and nota >= 9 and frequencia >= 75:
    print("Matrícula aprovada automaticamente.")
    print(f"O aluno tem {idade} anos, nota de {nota} e frequência de {frequencia}% — todas as condições básicas foram atendidas, portanto a matrícula é aprovada automaticamente.")

elif idade >= 18 and (nota >= 6 and frequencia >= 75):
    print("Matrícula aprovada")
    print(f"O aluno tem {idade} anos, nota de {nota} e frequência de {frequencia}% — todas as condições básicas foram atendidas, portanto a matrícula é aprovada normalmente.")

else:
    print("Matrícula negada pois não atende os requisitos mínimos.")