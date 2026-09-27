# AVA4 - Sistemas Embarcados

## Sistema de Semáforo com Contagem Regressiva

Projeto desenvolvido para a disciplina de Sistemas Embarcados da Universidade Veiga de Almeida.

O sistema foi desenvolvido no simulador Wokwi utilizando uma Raspberry Pi Pico e programação em MicroPython.

O projeto representa um semáforo controlado por botão. Durante o sinal vermelho, um display de 7 segmentos apresenta uma contagem regressiva de 9 até 0.

## Funcionamento

- O sistema inicia com o LED verde aceso.
- O botão inicia a sequência do semáforo.
- O LED verde é apagado.
- O LED amarelo permanece aceso durante 3 segundos.
- O LED vermelho é acionado.
- O display realiza a contagem regressiva de 9 até 0.
- Ao final da contagem, o display é apagado.
- O LED verde volta a acender.
- O sistema fica disponível para um novo acionamento.

## Componentes utilizados

- Raspberry Pi Pico;
- um botão de pressão;
- LED vermelho;
- LED amarelo;
- LED verde;
- três resistores de 220 ohms;
- display de 7 segmentos;
- fios de conexão;
- simulador Wokwi.

## Mapeamento dos pinos

### Semáforo

- GP0: LED vermelho;
- GP1: LED amarelo;
- GP2: LED verde;
- GP3: botão.

### Display de 7 segmentos

- GP4: segmento A;
- GP5: segmento B;
- GP6: segmento C;
- GP7: segmento D;
- GP8: segmento E;
- GP9: segmento F;
- GP10: segmento G;
- 3V3: terminal comum do display.

## Arquivos do projeto

- `main.py`: código desenvolvido em MicroPython;
- `diagram.json`: montagem do circuito no Wokwi;
- arquivos `.png`: registros dos testes realizados.

## Simulação

Projeto disponível no Wokwi:

COLE AQUI O LINK DO PROJETO WOKWI

## Autor

Matheus Freire de Oliveira Dutra
