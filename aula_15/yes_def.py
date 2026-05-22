#Desenvolva um sistemade pizzaria onde será recebido o preço total,um desconto de 10%, e ao final exiba o valor total do pedido com esse desconto;

#Declarar uma def (função) 

def calcular_total(nome,preco,desconto=0.10):
    valor_desconto = preco * desconto
    total = preco - valor_desconto
    print(f""" 💴 RECIBO 💴
          🥸 Pedido do cliente: {nome}
          💵Valor do pedido: R$ {preco}
          💷 Desconto aplicado: {desconto}
          🍕Total: R$ {total:.2f}
          """)

# Invocação da def
calcular_total("João", 45.90)
calcular_total("Maria", 38.50)
calcular_total("Pedro", 20)
calcular_total("Ana", 19)
calcular_total("Carlos", 9.99) 


