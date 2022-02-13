import random

full_domino_set = [[x, y] for x in range(0, 7) for y in range(x, 7)]
computer_dominoes = []
player_dominoes = []
stock_dominos = []
snake = []
who_starts = ""


def distribute_dominoes():
    global full_domino_set

    random.shuffle(full_domino_set)
    player_set = random.sample(full_domino_set, k=7)
    full_domino_set = [domino for domino in full_domino_set if domino not in player_set]
    computer_set = random.sample(full_domino_set, k=7)
    stock_pieces = [domino for domino in full_domino_set if domino not in computer_set]

    return player_set, computer_set, stock_pieces


def print_first_move(who_start, snake_domino):
    print("======================================================================")
    print("Stock size:", len(stock_dominos))
    print("Computer pieces:", len(computer_dominoes))
    print()
    print(snake_domino)
    print()
    print("Your pieces:")
    for key, domino in enumerate(player_dominoes):
        print(f"{key + 1}: {domino}")
    print()
    if who_start == "player":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")


while True:
    player_dominoes, computer_dominoes, stock_dominos = distribute_dominoes()
    if max(computer_dominoes) != max(player_dominoes):
        break

if max(computer_dominoes) > max(player_dominoes):
    snake = max(computer_dominoes)
    computer_dominoes.remove(snake)
    who_starts = "computer"
else:
    snake = max(player_dominoes)
    player_dominoes.remove(snake)
    who_starts = "player"

print_first_move(who_starts, snake)
