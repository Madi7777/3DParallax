import pygame

def main():
    pygame.init()  # Initialize pygame

    # Initialize music
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # Fullscreen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Cityscape")

    # Game variables 
    scroll = 0

    # Load background images 
    bg_images = []
    for i in range(1, 5):
        bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
        # Resizing image
        bg_image = pygame.transform.scale(bg_image,
            (int(bg_image.get_width() * (screen.get_height() / bg_image.get_height())),
            screen.get_height()))
        bg_images.append(bg_image)

    bg_width = bg_images[0].get_width()


    clock = pygame.time.Clock()
    FPS = 60

    def draw_bg():
        for x in range(5):
            speed = 1
            for i in bg_images:
                screen.blit(i, (x * bg_width - scroll * speed, 0))
                speed += 0.2
        

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        #Camera Scroll
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            scroll -= 5
        if key[pygame.K_RIGHT]:
            scroll += 5

        draw_bg()
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()