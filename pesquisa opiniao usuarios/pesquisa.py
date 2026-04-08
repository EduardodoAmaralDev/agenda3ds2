import time
import os
ruim = 0
bom = 0
exc = 0

# Entrada de dados(solicita aos usuários 50 opiniões)
for i in range(1, 51):
    nome = str(input("Digite seu nome: "))
    idade = input("Digite sua idade: ")
    while True: 
        opiniao = input("""Como foi seu atendimento? 
                   Digite 1 para Excelente;
                   Digite 2 para Bom;
                   Digite 3 para Ruim
                   """)
        #Verifica se o valor digitado foi 1, 2 ou 3, se não for repete a solicitação
        if opiniao in ["1", "2", "3"]:
            print(f"Opnião computada: {opiniao}")
            
            opiniao = int(opiniao) #Converte str em int para possibilitar os cálculos
            if opiniao == 1: 
                ruim += 1
            elif opiniao == 2:
                bom += 1
            else:
                exc += 1 
            break # Sai do loop se for válido
        else:
            print("Entrada inválida! Tente novamente.")
            
print(f"""  
        Foram computadas {i} opiniões.
        Ruim = {ruim} ou {100/i*ruim}%
        Bom = {bom} ou {100/i*bom}%
        Excelente = {exc} ou {100/i*exc}%""")
   

time.sleep(30)
os.system('cls')