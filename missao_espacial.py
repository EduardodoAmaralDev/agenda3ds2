# missao_espacial.py

# Entrada de dados
nome = input("Digite seu nome completo (astronauta da missão): ")
distancia = float(input("Digite a distância da viagem em km: "))
velocidade = float(input("Digite a velocidade média da nave em km/h: "))

# Verificação simples
if velocidade <= 0:
    print("Erro: a velocidade deve ser maior que zero.")
else:
    # Cálculos
    tempo_horas = distancia / velocidade
    tempo_dias = tempo_horas / 24

    # Saída de dados
    print(f"\nAstronauta {nome}, bem-vindo à simulação!")
    print(f"A viagem terá uma distância de {distancia:,.0f} km.")
    print(f"Com velocidade média de {velocidade:.0f} km/h, o tempo estimado é:")
    print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
    print("Boa sorte na missão!")