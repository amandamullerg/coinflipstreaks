import random
numberOfStreaks = 0
coinList = []

def coinFlip():
    flip = random.randint(0,1)
    if flip == 0:
        return 0
    else:
        return 1

for experimentNumber in range(10000):
    # lista com 100
    for flips in range(100):
        coinList.append(coinFlip()) # adiciona os resultados da função chamada já dentro do append pra lista
    
    # checkar os streaks
    streak = 0
    for coin in range(len(coinList)- 1):
        if coinList[coin] == coinList[coin + 1]: # compara o número com o próximo
            streak += 1
            if streak == 5: # repetiu 5x APÓS o 1o (6 numeros)
                numberOfStreaks += 1
                streak = 0
                break
        else:
            streak = 0
    coinList = [] # reseta a lista pra analisar uma nova
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
        
        
        

