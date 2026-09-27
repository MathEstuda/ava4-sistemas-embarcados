from machine import Pin
from time import sleep, sleep_ms

# --------------------------------------------------
# CONFIGURACAO DOS LEDS DO SEMAFORO
# --------------------------------------------------

led_vermelho = Pin(0, Pin.OUT)
led_amarelo = Pin(1, Pin.OUT)
led_verde = Pin(2, Pin.OUT)

# --------------------------------------------------
# CONFIGURACAO DO BOTAO
# --------------------------------------------------

# Botao ligado entre GP3 e GND
# Solto = 1
# Pressionado = 0
botao = Pin(3, Pin.IN, Pin.PULL_UP)

# --------------------------------------------------
# CONFIGURACAO DO DISPLAY DE 7 SEGMENTOS
# --------------------------------------------------

# Ordem dos segmentos: A, B, C, D, E, F, G
segmentos = [
    Pin(4, Pin.OUT),   # Segmento A
    Pin(5, Pin.OUT),   # Segmento B
    Pin(6, Pin.OUT),   # Segmento C
    Pin(7, Pin.OUT),   # Segmento D
    Pin(8, Pin.OUT),   # Segmento E
    Pin(9, Pin.OUT),   # Segmento F
    Pin(10, Pin.OUT)   # Segmento G
]

# Padroes dos numeros de 0 a 9
# O display e anodo comum:
# 0 = segmento aceso
# 1 = segmento apagado

numeros = [
    [0, 0, 0, 0, 0, 0, 1],  # 0
    [1, 0, 0, 1, 1, 1, 1],  # 1
    [0, 0, 1, 0, 0, 1, 0],  # 2
    [0, 0, 0, 0, 1, 1, 0],  # 3
    [1, 0, 0, 1, 1, 0, 0],  # 4
    [0, 1, 0, 0, 1, 0, 0],  # 5
    [0, 1, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 1, 1, 1, 1],  # 7
    [0, 0, 0, 0, 0, 0, 0],  # 8
    [0, 0, 0, 0, 1, 0, 0]   # 9
]


# --------------------------------------------------
# FUNCOES DO DISPLAY
# --------------------------------------------------

def mostrar_numero(numero):
    """Mostra um numero de 0 a 9 no display."""

    padrao = numeros[numero]

    for indice in range(7):
        segmentos[indice].value(padrao[indice])


def apagar_display():
    """Apaga todos os segmentos do display."""

    for segmento in segmentos:
        segmento.value(1)


# --------------------------------------------------
# FUNCOES DO SEMAFORO
# --------------------------------------------------

def estado_verde():
    """Acende somente o LED verde."""

    led_vermelho.off()
    led_amarelo.off()
    led_verde.on()

    apagar_display()

    print("Semaforo verde - aguardando acionamento do botao")


def estado_amarelo():
    """Mantem o LED amarelo aceso durante 3 segundos."""

    led_vermelho.off()
    led_verde.off()
    led_amarelo.on()

    apagar_display()

    print("Semaforo amarelo - aguarde")
    sleep(3)


def estado_vermelho():
    """Acende o LED vermelho e realiza a contagem de 9 ate 0."""

    led_verde.off()
    led_amarelo.off()
    led_vermelho.on()

    print("Semaforo vermelho - contagem regressiva")

    for numero in range(9, -1, -1):
        mostrar_numero(numero)
        print("Contagem:", numero)
        sleep(1)

    apagar_display()
    led_vermelho.off()


# --------------------------------------------------
# INICIALIZACAO
# --------------------------------------------------

estado_verde()

print("Sistema de semaforo iniciado")


# --------------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------------

while True:

    # O botao retorna 0 quando pressionado
    if botao.value() == 0:

        print("Botao pressionado")

        # Pequena pausa para evitar leituras instaveis
        sleep_ms(50)

        # Confirma que o botao permanece pressionado
        if botao.value() == 0:

            estado_amarelo()
            estado_vermelho()
            estado_verde()

            # Aguarda o usuario soltar o botao
            while botao.value() == 0:
                sleep_ms(20)

            # Pequeno intervalo contra acionamentos repetidos
            sleep_ms(200)

    sleep_ms(20)