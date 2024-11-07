import json

with open("faturamento.json", "r") as file:
    dados = json.load(file)

faturamentos = [dia["faturamento"] for dia in dados if dia["faturamento"] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor faturamento ocorrido em um dia do mês: {menor_faturamento}")
print(f"Maior faturamento ocorrido em um dia do mês: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
