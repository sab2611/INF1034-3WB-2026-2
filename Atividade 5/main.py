from pygame import *

init()
screen = display.set_mode((1280,720))

# Recursos

# batman_img = image.load("batman.png")
# batman_img = transform.scale(batman_img, (200,200))

# fonte = font.Font("batmfa__.fft", 50)




running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:
            running = False

    screen.fill(("#97D1FA"))

    # grama
    draw.rect(screen,"#489D25", (0, 600, 1280, 200))

    # sol
    draw.line(screen, "#FFF251", (10, 10), (190,190), 20)
    draw.circle(screen, "#FFF251", (100, 100),50)

    # casa
    draw.polygon(screen, "#F2883B", ((100, 300,), (200, 200), (300,300)))


    # Desenhando imagem

    # screen.blit(batman_img(300, 300))
    # fonte
    # audio

    display.update()









