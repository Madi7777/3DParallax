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
    paused = False

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (100, 100, 100)

    # Fonts
    font = pygame.font.SysFont("Arial", 50)
    button_font = pygame.font.SysFont("Arial", 30)

    # Pause menu buttons
    continue_button = pygame.Rect(
        screen.get_width() // 2 - 100, 350, 200, 60)

    quit_button = pygame.Rect(
        screen.get_width() // 2 - 100, 430, 200, 60)

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

    # Draw pause menu
    def draw_pause_menu():
        overlay = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

    # Title
        title = font.render("PAUSED, True, WHITE")
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 200))

    # Mouse 
    mouse_pos = pygame.mouse.get_pos()

    # Continue 
    if continue_button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (150, 150, 150),
                         continue_button, border_radius=10)
    else:
        pygame.draw.rect(screen, GRAY,
                         continue_button, border_radius=10)

    continue_text = button_font.render("CONTINUE", True, WHITE)

    screen.blit(continue_text, (continue_button.centerx - continue_text.get_width() 
                                // 2,continue_button.centery - continue_text.get_height() // 2))
    
    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = not paused

            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_BACKSPACE:
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