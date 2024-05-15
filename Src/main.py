import pygame
from pygame.locals import *

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

class CryptoAPI:
    @staticmethod
    def get_xrp_data():
        # Simulated XRP data
        return 1.2, 50000000000

    @staticmethod
    def get_btc_data():
        # Simulated Bitcoin data
        return 45000, 800000000000

    @staticmethod
    def get_doge_data():
        # Simulated Dogecoin data
        return 0.3, 6000000000

    @staticmethod
    def get_eth_data():
        # Simulated Ethereum data
        return 3000, 300000000000

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
    input_text_surface = font.render(text, True, BLACK)
    text_rect = input_text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(input_text_surface, text_rect)

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
                input_active = not input_active
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

    # Display options vertically
    options = ["XRP (Type 'xrp')", "Bitcoin (Type 'bitcoin')", "Dogecoin (Type 'dogecoin')", "Ethereum (Type 'ethereum')"]
    option_y = HEIGHT // 4
    for option in options:
        display_text(option, WIDTH // 2, option_y, font, BLACK)
        option_y += 50

    # Input box
    input_active = False
    input_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                input_active = not input_active
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        handle_crypto_input(input_text.lower())
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        # Render the input box
        input_rect = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 + 50, 300, 40)
        display_input_box(WIDTH//2 - 150, HEIGHT//2 + 50, 300, 40, font, input_text)

        pygame.display.update()

# Function to handle crypto input
def handle_crypto_input(text):
    if text == 'xrp':
        show_crypto_info("XRP")
    elif text == 'bitcoin':
        show_crypto_info("Bitcoin")
    elif text == 'dogecoin':
        show_crypto_info("Dogecoin")
    elif text == 'ethereum':
        show_crypto_info("Ethereum")
    else:
        print("Invalid input! Please type 'xrp', 'bitcoin', 'dogecoin', or 'ethereum'.")

# Function to display crypto information
def show_crypto_info(asset):
    if asset == "XRP":
        screen.fill(WHITE)
        display_text(asset + " Information", WIDTH//2, 50, font, BLACK)
        # Simulated XRP data
        current_price, market_cap = CryptoAPI.get_xrp_data()
        display_text("Market Value: $" + str(current_price), WIDTH//2, HEIGHT//2 - 25, font, BLACK)
        display_text("Market Cap: $" + str(market_cap), WIDTH//2, HEIGHT//2 + 25, font, BLACK)

    elif asset == "Bitcoin":
        screen.fill(WHITE)
        display_text(asset + " Information", WIDTH//2, 50, font, BLACK)
        # Simulated Bitcoin data
        current_price, market_cap = CryptoAPI.get_btc_data()
        display_text("Market Value: $" + str(current_price), WIDTH//2, HEIGHT//2 - 25, font, BLACK)
        display_text("Market Cap: $" + str(market_cap), WIDTH//2, HEIGHT//2 + 25, font, BLACK)

    elif asset == "Dogecoin":
        screen.fill(WHITE)
        display_text(asset + " Information", WIDTH//2, 50, font, BLACK)
        # Simulated Dogecoin data
        current_price, market_cap = CryptoAPI.get_doge_data()
        display_text("Market Value: $" + str(current_price), WIDTH//2, HEIGHT//2 - 25, font, BLACK)
        display_text("Market Cap: $" + str(market_cap), WIDTH//2, HEIGHT//2 + 25, font, BLACK)

    elif asset == "Ethereum":
        screen.fill(WHITE)
        display_text(asset + " Information", WIDTH//2, 50, font, BLACK)
        # Simulated Ethereum data
        current_price, market_cap = CryptoAPI.get_eth_data()
        display_text("Market Value: $" + str(current_price), WIDTH//2, HEIGHT//2 - 25, font, BLACK)
        display_text("Market Cap: $" + str(market_cap), WIDTH//2, HEIGHT//2 + 25, font, BLACK)

if __name__ == "__main__":
    main()
