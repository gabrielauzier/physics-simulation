import math
import os

mass = 1300
gravity = 9.8

def getSituationResult(case, ray, height):
    if case == 1:
        theta_rad = math.acos(1 - (height / ray))
        theta_deg = math.degrees(theta_rad)
        
        if 0 <= theta_deg <= 90:
            normalForce = mass * gravity * math.cos(theta_rad)
            
            print("\033[1;31mO carro não executa looping\033[m")
            print("\033[0;0m O carro para em\033[36m θ = %.0f °" %theta_deg)
            print("\033[0;0m Força normal\033[36m N = %.0f N"  %normalForce)
    
    elif case == 2:
        theta_rad = math.acos((2 / 3) * (1 - (height / ray)))
        theta_deg = math.degrees(theta_rad)
                
        if 90 <= theta_deg <= 180:
            velocity = math.sqrt((2/3) * gravity * (height-ray))
            
            print("\033[1;31mO carro não executa looping\033[m")
            print("\033[0;0m A força normal se anula em\033[36m θ = %.1f °" %theta_deg)
            print("\033[0;0m A velocidade do carro nessa posição é\033[36m v = %.1f m/s" %velocity)

    elif case == 3:
        normalB = mass * gravity * ((((2 * height) / ray) - 5))
        normalC = 2 * mass * gravity * (((height / ray) - 1))
        velB = math.sqrt(2 * gravity * (height - 2 * ray))
        velC = math.sqrt(2 * gravity * (height - ray))
        accelerationRadial = 2 * gravity * ((height / ray) - 1)
        accelerationTangent = gravity
        accelerationResult = math.sqrt(accelerationTangent ** 2 + accelerationRadial ** 2)
        
        print("\033[1;32mO carro executa o looping\033[m")
        print("\033[0;0m A velocidade em B é = \033[36m %.2f m/s" %velB)
        print("\033[0;0m A velocidade em C é = \033[36m %.2f m/s" %velC)
        print("\033[0;0m A força normal em B é = \033[36m %.0f N" %normalB)
        print("\033[0;0m A força normal em C é  \033[36m %.0f N" %normalC)
        print("\033[0;0m A aceleração tangencial em C é  \033[36m %.2f m/s²" %accelerationTangent)
        print("\033[0;0m A aceleração radial em C é  \033[36m %.2f m/s²" %accelerationRadial) 
        print("\033[0;0m A aceleração resultante em C é  \033[36m %.2f m/s²" %accelerationResult)

print("\033[33m")
print("OBS: ")
print("10m <= R <= 20m")
print("0 < h <= 5R")
print("\033[34m")
print("Forneça o Raio em metros")
print("Forneça a Altura em quantidades de Raios")
print("\033[0;0m")

while True:
    ray = float(input("R: "))
    if 10 <= ray <= 20:
        break
    else: 
      print("Raio fora do intervalo") 

while True:
    height = float(input("h: "))
    if 0 < height <= 5:
        break
    else:
        print("Altura fora do intervalo")
        
os.system('cls||clear')
print("\033[34m")
print("Dados: ")
print("R = %.1f m" %ray)
print("h = %.1f m ou h = %.1f R" %(height * ray, height))
print("\033[0;0m")

height = height * ray

# Situação 1 - Carro não executa looping e altura é menor que o raio
if height <= ray:
    getSituationResult(1, ray, height)

# Situação 2 - O carro não executa looping e a altura está entre o raio e o valor mínimo para o looping
if ray < height < 2.5 * ray:
    getSituationResult(2, ray, height)

# 3 o carro executa looping
if height >= 2.5 * ray:
    getSituationResult(3, ray, height)

print("\033[0;0m")
ans = input("Exit ")
os.system('cls||clear')