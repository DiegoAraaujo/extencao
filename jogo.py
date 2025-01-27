import turtle
import time
import random

# Configurações iniciais do jogo
tela = turtle.Screen()
tela.title("Jogo da Cobrinha")
tela.bgcolor("blue")
tela.setup(width=600, height=600)
tela.tracer(0)  # Atualização manual da tela

# Configuração da cobrinha
cobrinha = turtle.Turtle()
cobrinha.shape("square")
cobrinha.color("white")
cobrinha.penup()
cobrinha.goto(0, 0)
cobrinha.direcao = "parado"

# Comida da cobrinha
comida = turtle.Turtle()
comida.shape("circle")
comida.color("light blue")
comida.penup()
comida.goto(0, 100)

# Segmentos do corpo da cobrinha
segmentos = []

# Pontuação
pontuacao = 0
maior_pontuacao = 0

# Mostrar pontuação
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write(f"Pontuação: {pontuacao}  Maior pontuação: {maior_pontuacao}", align="center", font=("Courier", 24, "normal"))

# Funções para movimentar a cobrinha
def ir_para_cima():
    if cobrinha.direcao != "baixo":
        cobrinha.direcao = "cima"

def ir_para_baixo():
    if cobrinha.direcao != "cima":
        cobrinha.direcao = "baixo"

def ir_para_esquerda():
    if cobrinha.direcao != "direita":
        cobrinha.direcao = "esquerda"

def ir_para_direita():
    if cobrinha.direcao != "esquerda":
        cobrinha.direcao = "direita"

def mover():
    if cobrinha.direcao == "cima":
        cobrinha.sety(cobrinha.ycor() + 20)
    if cobrinha.direcao == "baixo":
        cobrinha.sety(cobrinha.ycor() - 20)
    if cobrinha.direcao == "esquerda":
        cobrinha.setx(cobrinha.xcor() - 20)
    if cobrinha.direcao == "direita":
        cobrinha.setx(cobrinha.xcor() + 20)

# Controles do teclado
tela.listen()
tela.onkey(ir_para_cima, "Up")
tela.onkey(ir_para_baixo, "Down")
tela.onkey(ir_para_esquerda, "Left")
tela.onkey(ir_para_direita, "Right")

# Loop principal do jogo
while True:
    tela.update()

    # Verificar colisão com a borda
    if (cobrinha.xcor() > 290 or cobrinha.xcor() < -290 or 
        cobrinha.ycor() > 290 or cobrinha.ycor() < -290):
        time.sleep(1)
        cobrinha.goto(0, 0)
        cobrinha.direcao = "parado"

        # Resetar o corpo da cobrinha
        for segmento in segmentos:
            segmento.goto(1000, 1000)  # Tira os segmentos da tela
        segmentos.clear()
        pontuacao = 0
        texto.clear()
        texto.write(f"Pontuação: {pontuacao}  Maior pontuação: {maior_pontuacao}", align="center", font=("Courier", 24, "normal"))

    # Verificar colisão com a comida
    if cobrinha.distance(comida) < 20:
        # Mover a comida para uma nova posição
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        # Adicionar um segmento ao corpo
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("green")
        novo_segmento.penup()
        segmentos.append(novo_segmento)

        # Atualizar a pontuação
        pontuacao += 10
        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
        texto.clear()
        texto.write(f"Pontuação: {pontuacao}  Maior pontuação: {maior_pontuacao}", align="center", font=("Courier", 24, "normal"))

    # Mover o corpo da cobrinha
    for index in range(len(segmentos) - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if len(segmentos) > 0:
        x = cobrinha.xcor()
        y = cobrinha.ycor()
        segmentos[0].goto(x, y)

    mover()

    # Verificar colisão com o próprio corpo
    for segmento in segmentos:
        if segmento.distance(cobrinha) < 20:
            time.sleep(1)
            cobrinha.goto(0, 0)
            cobrinha.direcao = "parado"

            # Resetar o corpo da cobrinha
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            segmentos.clear()
            pontuacao = 0
            texto.clear()
            texto.write(f"Pontuação: {pontuacao}  Maior pontuação: {maior_pontuacao}", align="center", font=("Courier", 24, "normal"))

    time.sleep(0.1)