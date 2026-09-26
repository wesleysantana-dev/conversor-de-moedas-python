
print("--- CONVERSOR DE MOEDAS ---")

dolar_hoje = 5.21 # Exemplo de valor
valor_reais = float(input("Digite o valor em R$ que deseja converter: "))

conversao = valor_reais / dolar_hoje

print(f"Com R$ {valor_reais:.2f} você pode comprar US$ {conversao:.2f}")
