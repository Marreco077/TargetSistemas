# 4 Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

def calcula_porcentagem(valor: float, total: float) -> float:
    return (valor / total) * 100


estados = ["SP", "RJ", "MG", "ES", "Outros"]
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

faturamento_total = sum(faturamento)

for i in range(len(estados)):
    porcentagem = calcula_porcentagem(faturamento[i], faturamento_total)
    print(f"Estado: {estados[i]} - {porcentagem:.2f}%")