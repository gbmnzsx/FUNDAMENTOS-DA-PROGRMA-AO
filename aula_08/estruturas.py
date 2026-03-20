# if (se) -> Verifica se uma informação é true. Se for ele executa o código 
# elif (senão se) -> É usado para testar várias condições. Ele só executa o código
# else(senão) -> Executa o código se a condiçõo if for false 

# idade_usuario = 15   
# # se o usuario for maior de 18 anos , eu vou passar a informacao;vc é maior de idade , senao vc e menor de idade 


# if idade_usuario >= 18:
#     print("voce e maior de idade")
# else:
#     print("voce e menor de idade")

idade = 73
if idade >= 18:
    print("voce e maior de idade")
elif idade >= 0 and idade < 18:
    print("voce e jovem de idade")
elif idade >= 70:
    print("voce e experiente de idade")
else:
     print("voce e menor de idade")