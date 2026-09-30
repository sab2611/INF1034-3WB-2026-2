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
    screen.fill(("#607EB3"))


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
    draw.rect(screen,"#2C264A", (0, 600, 1280, 200))

    # arvore


    # sol
    draw.line(screen, "#DCC7C4", (10, 10), (190,190), 10)
    draw.line(screen, "#DCC7C4", (10, 180), (190,10), 10)
    draw.line(screen, "#DCC7C4", (10, 90), (190,90), 7)
    draw.line(screen, "#DCC7C4", (90, 10), (90,190), 7)
    draw.circle(screen, "#DCC7C4", (mouse_x, mouse_y),50)

    # casa
    draw.polygon(screen, "#222C59", ((1000, 300,), (1100, 200), (1200,300)))
    draw.rect(screen, "#6F618E", (1000, 300, 200, 300))
    draw.rect(screen, "#343960", (1110, 480, 60, 120))
    draw.circle(screen, "#080818", (1160, 550), 5)
    draw.rect(screen, "#080818", (1030, 340, 60, 120))
    #draw.line(screen, "#6F618E", (1100, 100), (1030,90), 7)
    #draw.line(screen, "#6F618E", (100, 1100), (90,1030), 7)
    
    #nuvem
    draw.circle(screen, "#AB919F",  (nuvem_x, 100), 50)
    draw.circle(screen, "#AB919F",  (nuvem_x + 50, 100), 50)
    draw.circle(screen, "#AB919F",  (nuvem_x + 100, 100), 50)
    draw.circle(screen, "#AB919F",  (nuvem_x + 150, 100), 50)
    draw.circle(screen, "#AB919F",  (nuvem_x + 200, 100), 50)
    draw.circle(screen, "#AB919F",  (nuvem_x + 250, 100), 50)
 

    # RECURSOS #

    hollow_img = image.load("Atividade 5\hollowKnight.png")
    hollow_img = transform.scale(hollow_img, (200,200))

    # fonte = font.Font("batmfa__.fft", 50)    


    # Desenhando imagem

    screen.blit(hollow_img,(300, 300))
    # fonte
    # audio 



    display.update()









