import pygame
import random
import os
from tkinter import simpledialog

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("assets/cachorro.ico")
iron = pygame.image.load("assets/scooby.png")
fundo = pygame.image.load("assets/fundo2.jpg")
fundoStart = pygame.image.load("assets/fundoStart1.jpg")
fundoDead = pygame.image.load("assets/fundoDead1.webp")
monstro1 = pygame.image.load("assets/monstro1.png")
monstro2 = pygame.image.load("assets/monstro2.png")


tamanho = (900,700)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Scooby Doo")
pygame.display.set_icon(icone)
missileSound = pygame.mixer.Sound("assets/missile.wav")
explosaoSound = pygame.mixer.Sound("assets/explosao.wav")
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonteMorte = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("assets/ironsound.mp3")

branco = (255,255,255)
preto = (0, 0 ,0 )


def jogar(nome):
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 118
    posicaoYPersona = 202 
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    posicaoXMonstro1 = 400
    posicaoYMonstro1 = -240
    velocidadeMonstro1 = 1
    posicaoXMonstro2 = 400
    posicaoYMonstro2 = -240
    velocidadeMonstro2 = 1
    pontos = 0
    larguraPersona = 250
    alturaPersona = 127
    larguaMonstro1  = 152
    alturaMonstro1  = 218
    larguaMonstro2  = 152
    alturaMonstro2  = 218
    dificuldade  = 30



    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0     

                
        posicaoXPersona = posicaoXPersona + movimentoXPersona                        
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona >550:
            posicaoXPersona = 540
        
            
        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( iron, (posicaoXPersona, 500) )
        
        posicaoYMonstro1 = posicaoYMonstro1 + velocidadeMonstro1
        if posicaoYMonstro1 > 600:
            posicaoYMonstro1 = -240
            pontos = pontos + 1
            velocidadeMonstro1 = velocidadeMonstro1 + 1
            posicaoXMonstro1 = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)

        posicaoYMonstro2 = posicaoYMonstro2 + velocidadeMonstro2
        if posicaoYMonstro2 > 600:
            posicaoYMonstro2 = -240
            pontos = pontos + 1
            velocidadeMonstro2 = velocidadeMonstro2 + 1
            posicaoXMonstro2 = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
            
            
        tela.blit( monstro1, (posicaoXMonstro1, posicaoYMonstro1) )
                    
        tela.blit( monstro2, (posicaoXMonstro2, posicaoYMonstro2) )
        
        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsMonstro1X = list(range(posicaoXMonstro1, posicaoXMonstro1 + larguaMonstro1))
        pixelsMonstro1Y = list(range(posicaoYMonstro1, posicaoYMonstro1 + alturaMonstro1))
        pixelsMonstro2X = list(range(posicaoXMonstro2, posicaoXMonstro2 + larguaMonstro2))
        pixelsMonstro2Y = list(range(posicaoYMonstro2, posicaoYMonstro2 + alturaMonstro2))
        
        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsMonstro1Y).intersection(set(pixelsPersonaX))) ) > dificuldade:
            if len( list( set(pixelsMonstro1X).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)

        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsMonstro2Y).intersection(set(pixelsPersonaX))) ) > dificuldade:
            if len( list( set(pixelsMonstro2X).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        


        pygame.display.update()
        relogio.tick(60)

        

def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("Iron Man","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (35,50,200,50),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (90,50))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (330,482))

        
        
        pygame.display.update()
        relogio.tick(60)

start()