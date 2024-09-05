total_faturamento = 0
dias_com_faturamento = 0
import json
media = 0
with open('Desafio-Target/faturamento.json') as json_file:
	dados = json.load(json_file)

for i in dados:
    if float(i['valor']) > 0:
        total_faturamento += float(i['valor'])
        dias_com_faturamento += 1
media_mensal = total_faturamento / dias_com_faturamento

# Calcula o menor valor de faturamento
menor_valor = float(dados[0]['valor'])
for i in dados:
    if float(i['valor']) > 0 and float(i['valor']) < menor_valor:
        menor_valor = float(i['valor'])

# Calcula o maior valor de faturamento
maior_valor = float(dados[0]['valor'])
for i in dados:
    if float(i['valor']) > maior_valor:
        maior_valor = float(i['valor'])

# Calcula o número de dias com faturamento acima da média
dias_acima_media = 0
for i in dados:
    if float(i['valor']) > media_mensal:
        dias_acima_media += 1

print("O menor valor de faturamento: R$" + str(menor_valor))
print("O maior valor de faturamento: R$" + str(maior_valor))
print("Número de dias com faturamento acima da média: " + str(dias_acima_media))