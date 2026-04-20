import pygame
import random

# Pornește motorul grafic Pygame
pygame.init()

def genereaza_grila_culori():
    # Creăm o listă care va conține rândurile grilei noastre
    grila = []
    for y in range(10):
        rand_nou = []
        for x in range(10):
            # Generăm o culoare la întâmplare (coduri pentru Roșu, Verde, Albastru)
            culoare = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            rand_nou.append(culoare)
        grila.append(rand_nou)
    return grila

# Creăm fereastra de 500 pe 500 pixeli
fereastra = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Grila Culori (Se schimba la 5 secunde)")

# Generăm primele culori și setăm fereastra să ruleze
grila_culori = genereaza_grila_culori()
joc_activ = True

# Pornim cronometrul
timpul_trecut = pygame.time.get_ticks()

while joc_activ:
    # 1. Desenăm fundalul negru
    fereastra.fill((0, 0, 0))

    # 2. Desenăm fiecare pătrat în parte
    for y in range(10):
        for x in range(10):
            culoare_patrat = grila_culori[y][x]
            # Calculăm unde trebuie pus pătratul și ce mărime are (50x50)
            pozitie = (x * 50, y * 50, 50, 50)
            pygame.draw.rect(fereastra, culoare_patrat, pozitie)

    # 3. Afișăm pe ecran tot ce am desenat
    pygame.display.flip()

    # 4. Verificăm dacă s-au scurs 5 secunde (5000 milisecunde)
    timpul_curent = pygame.time.get_ticks()
    if timpul_curent - timpul_trecut >= 5000:
        grila_culori = genereaza_grila_culori()  # Regenerăm culorile
        timpul_trecut = timpul_curent            # Resetăm cronometrul pentru următoarele 5 secunde

    # 5. Verificăm dacă utilizatorul a apăsat butonul X ca să iasă
    for eveniment in pygame.event.get():
        if eveniment.type == pygame.QUIT:
            joc_activ = False

# Închidem programul corect
pygame.quit()