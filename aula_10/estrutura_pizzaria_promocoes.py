# Variáveis da pizzaria
FRETE = 2 #Constante Fake
pizza_sabor = input("Informe o sabor da pizza - [frango com requeijao] [calabresa] [mussarela] [banana com chocolate]:") 
pizza_tamanho = input("Informe o tamanho da pizza - [pequena], [média] , [grande]:")
dia_semana = input ("Informe o dia da semana - [qurta] [quinta] [sexta] [sabado] [domingo]:")

print(f" o sabor escolhido da pizza é {pizza_sabor} , o tamanho é {pizza_tamanho} e hoje é {dia_semana}")
# Promoções -> Estruturas Condicionais 

# Comprando qualquer pizza e qualquer tamanho no sábado, o refri é gratuito 
if dia_semana == "sabado": 
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O refri hoje é por conta da casa")
elif dia_semana == "domingo":
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O Frete e o refri hoje é por conta da casa")
elif pizza_sabor == "calabresa" and pizza_tamanho =="média" :
    print(f"🍕Pedido aceito com sucesso!")
    print(f"O frete hoje é por conta da casa")


  
# Comprando uma pizza de calabresa tamanho médio, em qualquer dia, o frete é gratuito.

# Comprando qualquer pizza de qualquer tamanho no domingo , o frete e o feri são gratuitos

