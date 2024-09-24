idade=int(input("Digite sua idade:"))
habilitacao=str(input("Você possui habilitação?"))
if idade>=18 and habilitacao=="sim":
    print("Você pode dirigir")
else:
    print("Você não pode dirigir, pois é menor de idade.")

