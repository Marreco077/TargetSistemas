import json

def calcula_faturamento(faturamento_diario):
    # filtrar os dias com faturamento igual a 0
    faturamento_valido = [f['valor'] for f in faturamento_diario if f['valor'] > 0]

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

    dias_acima_da_media = sum(1 for f in faturamento_valido if f > media_faturamento)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

with open('faturamento.json') as file:
    dados = json.load(file)

faturamento_diario = dados 

menor, maior, dias_acima_media = calcula_faturamento(faturamento_diario)

# resultados
print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
