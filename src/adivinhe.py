import pygame
import random

largura_tela = 800
altura_tela = 600

cor_fundo = (255, 255, 255)

emoji = "*"
cor_emoji = (0, 0, 0)
tamanho_emoji = 30
velocidade_emoji = 5
quantidade_emojis = 100

def exibir_chuva_de_emojis():
    pygame.init()
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Chuva de Emojis")

    emojis = []

    for _ in range(quantidade_emojis):
        x = random.randint(0, largura_tela)
        y = random.randint(-altura_tela, 0)
        emojis.append([x, y])

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        tela.fill(cor_fundo)

        for emoji_pos in emojis:
            emoji_pos[1] += velocidade_emoji
            pygame.draw.rect(tela, cor_emoji, (emoji_pos[0], emoji_pos[1], tamanho_emoji, tamanho_emoji))
            tela.blit(pygame.font.SysFont(None, tamanho_emoji).render(emoji, True, cor_emoji), emoji_pos)

            if emoji_pos[1] > altura_tela:
                emoji_pos[1] = random.randint(-altura_tela, 0)
                emoji_pos[0] = random.randint(0, largura_tela)

        pygame.display.flip()
        clock.tick(60)

def adivinhe_o_numero():
    numero_secreto = 22

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Estou pensando em um número. Tente adivinhar!")

    while True:
        try:
            palpite = int(input("Digite o seu palpite: "))

            if palpite < numero_secreto:
                print("O número que você digitou é menor. Tente novamente!")
            elif palpite > numero_secreto:
                print("O número que você digitou é maior. Tente novamente!")
            else:
                print(f"Parabéns! Você acertou!")
                exibir_chuva_de_emojis()
                break

        except ValueError:
            print("Por favor, digite um número válido.")

    print("Obrigado por jogar!")

adivinhe_o_numero()
