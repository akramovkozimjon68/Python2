import pygame
import random
import sys

# Pygame-ni ishga tushirish
pygame.init()

# Ekran o'lchamlarini belgilash
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix - Kozimjon")

# Ranglar
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Matrix yashil rangi
DARK_GREEN = (0, 100, 0) # Orqa fondagi so'nish effekti uchun

# Shriftni tanlash (kompyuterda mavjud standart shrift)
font_size = 20
font = pygame.font.SysFont('courier', font_size, bold=True)

# Yoziladigan so'z
text = "Kozimjon"

# Har bir ustun uchun boshlang'ich Y koordinatasini saqlash
# Ekran kengligini shrift o'lchamiga bo'lib, nechta ustun sig'ishini hisoblaymiz
columns = WIDTH // font_size
drops = [random.randint(-HEIGHT, 0) for _ in range(columns)]

# Soat (FPS)ni boshqarish uchun
clock = pygame.time.Clock()

running = True
while running:
    # Oynani yopishni tekshirish
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekranni qora rang bilan to'ldirish (yoki yarim shaffof qora bilan)
    # Yarim shaffof qora (alpha=50) oldingi harflarni sekin o'chirib, iz qoldiradi
    fade_surface = pygame.Surface((WIDTH, HEIGHT))
    fade_surface.set_alpha(50)
    fade_surface.fill(BLACK)
    screen.blit(fade_surface, (0, 0))

    # Har bir ustun uchun harakatni chizish
    for i in range(len(drops)):
        # Tasodifiy ravishda ba'zi ustunlarga so'zni yozamiz, ba'zilariga tasodifiy harf
        if random.random() > 0.8:
            char = random.choice(text)
        else:
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*")

        # Harfni render qilish
        text_surface = font.render(char, True, GREEN)
        
        # X va Y koordinatalarini hisoblash
        x = i * font_size
        y = drops[i] * font_size
        
        # Ekranga chizish
        screen.blit(text_surface, (x, y))

        # Ustun pastga tushib, ekrandan chiqib ketsa, uni yuqoriga qaytarish
        if y > HEIGHT and random.random() > 0.975:
            drops[i] = 0
        
        # Y koordinatasini pastga siljitish
        drops[i] += 1

    # Ekranni yangilash
    pygame.display.flip()
    
    # Sekundiga 30 kadr (FPS) tezlikda ishlashi uchun
    clock.tick(79)

# O'yinni yopish
pygame.quit()
sys.exit()