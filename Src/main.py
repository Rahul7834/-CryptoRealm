import pygame
from pygame.locals  import *

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CryptoQuest")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Set up fonts
font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

# Function to display text on screen
def display_text(text, x, y, font, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to display text input box
def display_input_box(x, y, width, height, font, text):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)
    display_text(text, x + width // 2, y + height // 2, font, BLACK)

# Main game loop
def main():
    running = True
    input_active = False
    input_text = ""
    while running:
        screen.fill(WHITE)
        display_text("CryptoQuest", WIDTH//2, 50, font, BLACK)
        display_text("Welcome to CryptoQuest! You find yourself in a world of digital currencies.", WIDTH//2, 120, small_font, BLACK)
        display_text("Your mission is to navigate through various crypto assets. Type 'start' to begin.", WIDTH//2, 150, small_font, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        handle_input(input_text)
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        # Render the input box
        input_rect = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 50, 300, 40)
        display_input_box(WIDTH//2 - 150, HEIGHT//2 + 50, 300, 40, font, input_text)

        pygame.display.update()

    pygame.quit()

# Function to handle user input
def handle_input(text):
    if text.strip().lower() == 'start':
        start_game()
    else:
        print("Invalid input! Type 'start' to begin.")

# Function to start the game
def start_game():
    screen.fill(WHITE)
    display_text("Choose your crypto asset:", WIDTH//2, 50, font, BLACK)
    display_text("XRP (Press 'x')", WIDTH//4, HEIGHT//2, font, BLACK)
    display_text("BitCoin (Press 'b')", WIDTH//4 * 2, HEIGHT//2, font, BLACK)
    display_text("DogeCoin (Press 'd')", WIDTH//4 * 3, HEIGHT//2, font, BLACK)
    display_text("Ethereum (Press 'e')", WIDTH//4 * 4, HEIGHT//2, font, BLACK)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    show_crypto_info("XRP")
                elif event.key == pygame.K_b:  
                    show_crypto_info("BitCoin")
                elif event.key == pygame.K_d:
                    show_crypto_info("DogeCoin")
                elif event.key == pygame.K_e:
                    show_crypto_info("Ethereum")

        pygame.display.update()

# Function to display crypto information
def show_crypto_info(asset):
    screen.fill(WHITE)
    if asset == "XRP":
        display_text("XRP Information", WIDTH//2, 50, font, BLACK)
        display_text("Value", WIDTH//4, HEIGHT//2, font, BLACK)
        display_text("MarketCap", WIDTH//4 * 3, HEIGHT//2, font, BLACK)
    elif asset == "BitCoin":
        display_text("BitCoin Information", WIDTH//2, 50, font, BLACK)
        display_text("Value", WIDTH//4, HEIGHT//2, font, BLACK)
        display_text("MarketCap", WIDTH//4 * 3, HEIGHT//2, font, BLACK)
    # Add similar blocks for DogeCoin and Ethereum

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

if __name__ == "__main__":
    main()
