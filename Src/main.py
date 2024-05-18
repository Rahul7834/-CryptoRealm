import pygame
import random
import time

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

# Define cryptocurrency classes
class Cryptocurrency:
    def __init__(self, name, value, market_cap):
        self.name = name
        self.value = value
        self.market_cap = market_cap

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_market_cap(self):
        return self.market_cap

    def update_value(self):
        change_percent = random.uniform(-0.10, 0.10)  # Random change between -10% and +10%
        self.value *= (1 + change_percent)

# Create instances of cryptocurrencies
xrp = Cryptocurrency("XRP", 1.2, 50000000000)
bitcoin = Cryptocurrency("Bitcoin", 45000, 800000000000)
dogecoin = Cryptocurrency("Dogecoin", 0.3, 6000000000)
ethereum = Cryptocurrency("Ethereum", 3000, 300000000000)

cryptocurrencies = [xrp, bitcoin, dogecoin, ethereum]

# Global variable for the user's balance and portfolio
user_balance = 25000
user_portfolio = {xrp: 0, bitcoin: 0, dogecoin: 0, ethereum: 0}

# Function to display text on screen
def display_text(text, x, y, font, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to display text input box
def display_input_box(x, y, width, height, font, text):
    pygame.draw.rect(screen, GRAY, (x, y, width, height))
    pygame.draw.rect(screen, BLACK, (x, y, width, height), 2)
    input_text_surface = font.render(text, True, BLACK)
    text_rect = input_text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(input_text_surface, text_rect)

# Function to display the money bar
def display_money_bar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 40))
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, 40), 2)
    text_surface = font.render("Balance: $" + str(round(user_balance, 2)), True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 20))
    screen.blit(text_surface, text_rect)

# Function to display the portfolio
def display_portfolio():
    screen.fill(WHITE)
    display_text("Portfolio", WIDTH // 2, 50, font, BLACK)
    y_offset = 100
    for crypto, amount in user_portfolio.items():
        value = crypto.get_value() * amount
        display_text(f"{crypto.get_name()}: {amount} units - Value: ${round(value, 2)}", WIDTH // 2, y_offset, font, BLACK)
        y_offset += 40
    pygame.display.update()

# Function to handle user input
def handle_input(text):
    if text.strip().lower() == 'start':
        start_game()
    else:
        print("Invalid input! Type 'start' to begin.")

# Function to handle crypto input
def handle_crypto_input(input_text):
    if input_text.startswith('buy'):
        buy_crypto(input_text.split()[1].lower())
    elif input_text == 'xrp':
        show_crypto_info(xrp)
    elif input_text == 'bitcoin':
        show_crypto_info(bitcoin)
    elif input_text == 'dogecoin':
        show_crypto_info(dogecoin)
    elif input_text == 'ethereum':
        show_crypto_info(ethereum)
    else:
        print("Invalid input! Please type 'xrp', 'bitcoin', 'dogecoin', or 'ethereum'.")

# Function to display crypto information
def show_crypto_info(crypto):
    # 10% chance for the selected crypto to increase its value 10x
    if random.random() < 0.10:
        crypto.value *= 10
        print(f"Lucky you! {crypto.get_name()} value increased 10x!")

    screen.fill(WHITE)
    display_text(crypto.get_name() + " Information", WIDTH // 2, 70, font, BLACK)
    display_text("Market Value: $" + str(round(crypto.get_value(), 2)), WIDTH // 2, HEIGHT // 2 - 50, font, BLACK)
    display_text("Market Cap: $" + str(crypto.get_market_cap()), WIDTH // 2, HEIGHT // 2 - 15, font, BLACK)
    display_text("Purchase (Type 'buy " + crypto.get_name().lower() + "')", WIDTH // 2, HEIGHT // 2 + 20, font, BLACK)
    input_text = ""
    display_input_box(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40, font, input_text)
    pygame.display.update()  # Update the display

# Function to buy cryptocurrency
def buy_crypto(crypto_name):
    global user_balance
    crypto = None
    if crypto_name == 'xrp':
        crypto = xrp
    elif crypto_name == 'bitcoin':
        crypto = bitcoin
    elif crypto_name == 'dogecoin':
        crypto = dogecoin
    elif crypto_name == 'ethereum':
        crypto = ethereum
    else:
        print("Invalid cryptocurrency name!")
        return

    # Clear the screen
    screen.fill(WHITE)

    # Display text for buying
    display_text(f"How much {crypto_name.upper()} would you like to buy?", WIDTH // 2, HEIGHT // 3, font, BLACK)
    display_text("Press ENTER to confirm your purchase.", WIDTH // 2, HEIGHT // 2, small_font, BLACK)

    # Input box for quantity
    input_active = True
    input_text = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    try:
                        quantity = int(input_text)
                        if quantity <= 0:
                            print("Invalid quantity! Quantity must be greater than zero.")
                        else:
                            total_cost = crypto.get_value() * quantity
                            if user_balance >= total_cost:
                                user_balance -= total_cost
                                user_portfolio[crypto] += quantity
                                print(f"You bought {quantity} {crypto.get_name()} for ${total_cost}. Your balance is now ${user_balance}.")
                            else:
                                print("Insufficient balance!")
                    except ValueError:
                        print("Invalid input! Please enter a valid integer quantity.")
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    input_text += event.unicode

        # Render the input box
        input_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40)
        display_input_box(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40, font, input_text)

        pygame.display.update()

    # After buying, move to the options screen
    options_screen()

# Function to show the options screen
def options_screen():
    screen.fill(WHITE)
    display_text("Options", WIDTH // 2, HEIGHT // 4, font, BLACK)
    display_text("1. Check Portfolio", WIDTH // 2, HEIGHT // 2 - 50, font, BLACK)
    display_text("2. Buy More", WIDTH // 2, HEIGHT // 2, font, BLACK)
    display_text("3. Trade", WIDTH // 2, HEIGHT // 2 + 50, font, BLACK)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    display_portfolio()
                elif event.key == pygame.K_2:
                    start_game()
                elif event.key == pygame.K_3:
                    sell_screen()

# Function to show the trade screen
def sell_screen():
    screen.fill(WHITE)
    display_text("Choose cryptocurrency to sell:", WIDTH // 2, HEIGHT // 4, font, BLACK)
    display_text("1. XRP", WIDTH // 2, HEIGHT // 2 - 50, font, BLACK)
    display_text("2. Bitcoin", WIDTH // 2, HEIGHT // 2, font, BLACK)
    display_text("3. Dogecoin", WIDTH // 2, HEIGHT // 2 + 50, font, BLACK)
    display_text("4. Ethereum", WIDTH // 2, HEIGHT // 2 + 100, font, BLACK)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choose_crypto_to_sell(xrp)
                elif event.key == pygame.K_2:
                    choose_crypto_to_sell(bitcoin)
                elif event.key == pygame.K_3:
                    choose_crypto_to_sell(dogecoin)
                elif event.key == pygame.K_4:
                    choose_crypto_to_sell(ethereum)

# Function to choose the cryptocurrency to sell
def choose_crypto_to_sell(crypto):
    screen.fill(WHITE)
    display_text(f"Enter the amount of {crypto.get_name()} to sell:", WIDTH // 2, HEIGHT // 4, font, BLACK)
    pygame.display.update()

    input_active = True
    input_text = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                    try:
                        amount_to_sell = int(input_text)
                        if amount_to_sell < 0 or amount_to_sell > user_portfolio[crypto]:
                            print("Invalid amount!")
                        else:
                            sell_crypto(crypto, amount_to_sell)
                    except ValueError:
                        print("Invalid input! Please enter a valid integer quantity.")
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    input_text += event.unicode

        # Render the input box
        input_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 40)
        display_input_box(WIDTH // 2 - 150, HEIGHT // 2, 300, 40, font, input_text)

        pygame.display.update()

# Function to sell cryptocurrency
def sell_crypto(crypto, amount):
    global user_balance
    crypto_value = crypto.get_value()
    total_sale = amount * crypto_value
    user_balance += total_sale
    user_portfolio[crypto] -= amount
    print(f"You sold {amount} {crypto.get_name()} for ${total_sale}. Your balance is now ${user_balance}.")
    options_screen()

# Function to start the game
def start_game():
    screen.fill(WHITE)
    display_text("Choose your crypto asset:", WIDTH // 2, 100, font, BLACK)

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
        input_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40)
        display_input_box(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40, font, input_text)

        pygame.display.update()

# Function to simulate an internet collapse
def simulate_internet_collapse():
    collapse_percent = random.uniform(0.30, 0.50)  # Decrease between 30% and 50%
    for crypto in cryptocurrencies:
        crypto.value *= (1 - collapse_percent)
    print("Internet collapse! All cryptocurrency values have dipped significantly.")

# Function to update cryptocurrency values every 10 seconds
def update_crypto_values():
    while True:
        if random.random() < 0.01:  # 1% chance of internet collapse
            simulate_internet_collapse()
        else:
            for crypto in cryptocurrencies:
                crypto.update_value()
        time.sleep(10)

# Main game loop
def main():
    global user_balance  # Declare global variable user_balance

    # Start the crypto value update in a separate thread
    import threading
    threading.Thread(target=update_crypto_values, daemon=True).start()

    running = True
    input_active = False
    input_text = ""
    while running:
        screen.fill(WHITE)
        display_money_bar()  # Display the money bar
        display_text("CryptoQuest", WIDTH // 2, 200, font, BLACK)
        display_text("Welcome to CryptoQuest! You find yourself in a world of digital currencies.", WIDTH // 2, 270, small_font, BLACK)
        display_text("Your mission is to navigate through various crypto assets. Type 'start' to begin.", WIDTH // 2, 300, small_font, BLACK)

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
        input_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40)
        display_input_box(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 40, font, input_text)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()