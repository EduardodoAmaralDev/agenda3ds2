import time
import os
num = int(input("Digite o número que deseja ver a tabuada "))
i = 1

while i <= 10:
    time.sleep(0.5)
    print(f"{num} X {i} = {num*i}")
    i += 1

time.sleep(3)
os.system('cls')
