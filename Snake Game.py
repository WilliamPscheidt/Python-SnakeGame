import os
import time
import random
import keyboard

campo = (['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"],['#', '#', '#', '#', '#', '#', "#", "#"])
vidas = 4
score = 0

def limparTela():
    os.system('cls')

def printCampo():
    limparTela()
    print("Pontos:", score, " | Vidas: ", vidas)
    for i in range(14):
        print(campo[i])

def spawnPlayer(): 
    global playerPosX  
    global playerPosY 
    playerPosY = random.sample(range(7), k=1)[0]
    playerPosX = random.sample(range(14), k=1)[0]
    campo[playerPosX][playerPosY] = '$'

def spawnComida():
    global comidaPosX
    global commidaPosY
    commidaPosY = random.sample(range(7), k=1)[0]
    comidaPosX = random.sample(range(14), k=1)[0]
    campo[comidaPosX][commidaPosY] = '@'

def removerVida():
    global vidas
    if(vidas <= 1):
        print("Infelizmente você perdeu o game =(")
    print("Você perdeu uma vida!")
    vidas -= 1

def moverJogador(movimento):
    global playerPosY
    global playerPosX
    global score
    campo[playerPosX][playerPosY] = '#'

    if(movimento == 'd'):
        if (playerPosY >= 7):
            removerVida()
            return
        playerPosX = playerPosX
        playerPosY = playerPosY + 1
        campo[playerPosX][playerPosY] = '$'
        if (playerPosX == comidaPosX and playerPosY == commidaPosY):
            campo[comidaPosX][commidaPosY] = '#'
            score = score + 1
            spawnComida()
    elif(movimento == 'a'):
        if (playerPosY <= 0):
            removerVida()
            return
        playerPosX = playerPosX
        playerPosY = playerPosY - 1
        campo[playerPosX][playerPosY] = '$'
        if (playerPosX == comidaPosX and playerPosY == commidaPosY):
            campo[comidaPosX][commidaPosY] = '#'
            score = score + 1
            spawnComida()
    elif(movimento == 'w'):
        if (playerPosX <= 0):
            removerVida()
            return
        playerPosX = playerPosX - 1
        playerPosY = playerPosY
        campo[playerPosX][playerPosY] = '$'
        if (playerPosX == comidaPosX and playerPosY == commidaPosY):
            campo[comidaPosX][commidaPosY] = '#'
            score = score + 1
            spawnComida()
    elif(movimento == 's'):
        if (playerPosX >= 13):
            removerVida()
            return
        playerPosX = playerPosX + 1
        playerPosY = playerPosY
        campo[playerPosX][playerPosY] = '$'
        if (playerPosX == comidaPosX and playerPosY == commidaPosY):
            campo[comidaPosX][commidaPosY] = '#'
            score = score + 1
            spawnComida()
    else:
        print("Movimento inválido")

    printCampo()

spawnComida()
spawnPlayer()
printCampo()

while True:
    if (vidas == 0):
        limparTela()
        print("Gameover, você perdeu!")
    else:
        if keyboard.is_pressed('d'):
            time.sleep(0.1)
            moverJogador("d")
        if keyboard.is_pressed('a'):
            time.sleep(0.1)
            moverJogador("a")
        if keyboard.is_pressed('w'):
            time.sleep(0.1)
            moverJogador("w")
        if keyboard.is_pressed('s'):
            time.sleep(0.1)
            moverJogador("s")
