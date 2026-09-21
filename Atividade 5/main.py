from pygame import*

init()
screen = display.set_mode((1280,720))
running = True
clock = time.Clock()
nuvem_x = 640

while running:
    clock.tick(30)
    for ev in event.get():
        if ev.type == QUIT:
            running = False
    screen.fill(("#97D1FA"))

# RECURSOS #

# batman_img = image.load("batman.png")
# batman_img = transform.scale(batman_img, (200,200))

# fonte = font.Font("batmfa__.fft", 50)    


    # FÍSICA #
    dt = clock.get_time()/1000
    keys = key.get_pressed()

    if keys[K_RIGHT]:
        nuvem_x = nuvem_x + 100 * dt 
    elif keys[K_LEFT]:
        nuvem_x = nuvem_x - 100 * dt 

    mouse_x, mouse_y = mouse.get_pos()


    # DESENHO #
    # grama
    draw.rect(screen,"#489D25", (0, 600, 1280, 200))

    # sol
    draw.line(screen, "#FFF251", (10, 10), (190,190), 20)
    draw.circle(screen, "#FFF251", (mouse_x, mouse_y),50)

    # casa
    draw.polygon(screen, "#F2883B", ((100, 300,), (200, 200), (300,300)))

    #nuvem
    draw.circle(screen, "#FFFFFF",  (nuvem_x, 100), 50)


    # Desenhando imagem

    # screen.blit(batman_img(300, 300))
    # fonte
    # audio 



    display.update()









