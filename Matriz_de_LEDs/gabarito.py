import RPi.GPIO as GPIO
from time import sleep
from copy import deepcopy

class MatrizLed():
    """
    MatrizLed - Biblioteca para se utilizar o display de leds 8x8 dg-d0338no
    """
    def __init__(self, delay_var=1e-3):
        # Mapeia linha -> pino na raspberry
        self.lin = {0: 12, 1: 3, 2: 27, 3: 4, 4: 26, 5: 17, 6: 6, 7: 21}
        # Mapeia coluna -> pino na raspberry
        self.col = {0: 19, 1: 13, 2: 16, 3: 22, 4: 20, 5: 10, 6: 2, 7: 5}
        # Delay de varredura do display
        self.delay_var = delay_var
        
        ## Configuracao das GPIOs
        GPIO.setwarnings(False) # desabilita warnings
        GPIO.setmode(GPIO.BCM) # seta a numeracao dos pinos como BCM
        GPIO.setup([v for v in self.lin.values()], GPIO.OUT) # seta os pinos das linhas como saida
        GPIO.setup([v for v in self.col.values()], GPIO.OUT) # seta os pinos das colunas como saida
        GPIO.output([v for v in self.lin.values()], GPIO.LOW) # coloca os pinos em LOW
        GPIO.output([v for v in self.col.values()], GPIO.LOW) # coloca os pinos em LOW

        # Telas padrao
        self.tela = {'A': [[0,0,0,0,0,0,0,0],
                           [1,1,1,1,1,1,1,0],
                           [1,1,1,1,1,1,1,1],
                           [0,0,1,1,0,1,1,1],
                           [0,0,1,1,0,1,1,1],
                           [1,1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1,0],
                           [0,0,0,0,0,0,0,0]],
                     'D': [[0,0,0,0,0,0,0,0],
                           [1,1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1,1],
                           [1,1,0,0,0,0,1,1],
                           [1,1,1,0,0,1,1,1],
                           [1,1,1,1,1,1,1,1],
                           [0,1,1,1,1,1,1,0],
                           [0,0,0,0,0,0,0,0]],
                     ' ': [[0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0]]}

    def acende_lin(self, r):
        GPIO.output(self.lin[r], GPIO.HIGH)

    def apaga_lin(self, r):
        GPIO.output(self.lin[r], GPIO.LOW)

    def acende_col(self, c):
        GPIO.output(self.col[c], GPIO.LOW)

    def apaga_col(self, c):
        GPIO.output(self.col[c], GPIO.HIGH)

    def pinta(self, tela, ms=1000):
        N = round(ms/8)
        for k in range(N):
            for i in range(8):
                self.acende_lin(i)
                for j in range(8):
                    if tela[i][j] == 1:
                        self.acende_col(j)
                    else:
                        self.apaga_col(j)
                sleep(self.delay_var)
                self.apaga_lin(i)

    def escreve(self, msg, ms=1000):
        for letra in msg:
            self.pinta(M.tela[letra], ms)

    def pinta_scroll(self, tela, ms=250):
        tela1 = deepcopy(self.tela[' '])
        tela2 = deepcopy(tela)
        for k in range(8):
            self.pinta(tela1, ms)
            tela1.pop()
            tela1.insert(0,tela[7-k])
        for k in range(8):
            self.pinta(tela2, ms)
            tela2.pop()
            tela2.insert(0, [0,0,0,0,0,0,0,0])

    def escreve_scroll(self, msg, ms=75):
        for letra in msg:
            self.pinta_scroll(M.tela[letra], ms)

if __name__ == '__main__':
    M = MatrizLed()
    while True:
        M.escreve("ADA ")
        M.escreve_scroll("ADA ")

