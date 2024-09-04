# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
preço = int(input('qual o valor do produto? '))
imp = preço * 0.12
p_final = preço + imp

print(f"com o imposto de 12%, o preço final do produto é R${p_final:.2f}")
