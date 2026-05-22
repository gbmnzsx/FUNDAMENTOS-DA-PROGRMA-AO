idade = 20
cadastro=True
tipo_veiculo = "grande"
cliente_vip=True


##regra de negócio: para entrada automática, o cliente deve estar cadastrado, ter 20 anos ou mais, possuir um veículo pequeno, médio ou grande e ser cliente VIP. Para entrada manual, o cliente deve estar cadastrado, ter menos de 20 anos, possuir um veículo médio e não ser cliente VIP. Caso contrário, a entrada é negada.




# entrada automática (VIP)
if idade >= 20 and cadastro == True and (tipo_veiculo == "pequeno" or tipo_veiculo == "medio" or tipo_veiculo == "grande") and cliente_vip == True:
    print("entrada liberada automaticamente")
    print(f"todos os requisitos foram atendidos, {idade} anos, veículo {tipo_veiculo}, cliente VIP: {cliente_vip}, entrada liberada automaticamente ")


# entrada manual (não VIP)
elif cadastro == True and idade < 20 and tipo_veiculo == "grande":
    print(f"o cliente atende os requisitos mínimos, {idade} anos, veículo {tipo_veiculo},{cadastro}cadastro, entrada liberada de maneira manual")

#entrada negada
else:
    print("o cliente não atende os requisitos mínimos,  anos, veículo , entrada negada")



   



