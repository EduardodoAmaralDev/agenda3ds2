import time
import os
num = int(input("Digite o número que deseja ver a tabuada "))

for i in range(1, 11):
    time.sleep(0.5)    
    print(f"{num} X {i} = {num*i}")
  
time.sleep(3)
os.system('cls')