import os
from random import choice
from typing import List

winning_moves = {
    "r": "s",
    "p": "r",
    "s": "p",
}

# name of computer in the final message
computerName = "Billy Bob Joe"
# name of the first player
player1Name = "Player 1"
# name of the second player
player2Name = "Player 2"

#
winMessage = "The winner is"
sgPlayerMessage = "SINGLEPLAYER"
mlPlayerMessage = "MULTIPLAYER"
settingsMessage = "SETTINGS"

movePrompt = "Choose your move (rock, paper, scissors)"
confirmationPrompt = "Press enter to continue"


def settings() -> None:
    """Setup the settings for the game"""

    cls(settingsMessage)
    print("1: Computer Name")
    print("2: Win Message")
    print("3: Player 1 Name")
    print("4: Player 2 Name")
    print("5: Singleplayer Message")
    print("6: Multiplayer Message")
    print("7: Prompt Message")
    print("8: Confirmation Message")
    print("0: Exit")

    option = int(input("Please choose an option: "))
    if option == 0:
        # if break: exit the function
        return None
    cls(settingsMessage)
    # get the new value
    matchSetting(option)


def matchSetting(option):
    inp = input("Please enter your new value: ")
    match option:
        case 1:
            global computerName
            computerName = inp
        case 2:
            global winMessage
            winMessage = inp
        case 3:
            global player1Name
            player1Name = inp
        case 4:
            global player2Name
            player2Name = inp
        case 5:
            global sgPlayerMessage
            sgPlayerMessage = inp
        case 6:
            global mlPlayerMessage
            mlPlayerMessage = inp
        case 7:
            global movePrompt
            movePrompt = inp
        case 8:
            global confirmationPrompt
            confirmationPrompt = inp
    settings()


def cls(message: str = None) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--------------------")
    if message is not None:
        print(message) if message is not None else None
        print("--------------------")


def printMove(move: str) -> str:
    match move[0]:
        case 's':
            return "scissors"
        case 'r':
            return "rock"
        case 'p':
            return "paper"
        case _:
            raise ValueError("Invalid move")


def rps(player1: str, player2: str) -> int:
    """The actual game logic, it returns the winner 
    as a representation of an int
    0: draw
    1: player 1
    2: player 2

    Args:
        player1 (str): the first player's move
        player2 (str): the second player's move

    Returns:
        int: the winner
    """
    # get first char
    player1 = player1[0]
    player2 = player2[0]
    # if they are the same, it's a draw
    if player1 == player2:
        return 0
    # if player 1's move is the value to player 2's key, player 1 wins
    for key in winning_moves.keys():
        print(key, winning_moves[key])
    return 1 if winning_moves[player1] == player2 else 2


def main() -> None:
    # print the main menu screen
    cls("MAIN MENU")
    print("Welcome to Rock, Paper, Scissors!")
    print("1: Multiplayer")
    print("2: Singleplayer")
    print("3: Settings")
    print("0: Exit")
    # get the user's choice for the game
    typ = int(input("Choose your type: "))
    match typ:
        case 0:
            # exit the game if the user chooses 0
            return
        case 1:
            # run a multiplayer game
            multiGame()
        case 2:
            sgGame()
        case 3:
            # run the settings menu
            settings()
    # recursively play the game again if the user does not chose 0.
    main()


def printPlayers(move1: str, move2: str, computer: bool = False) -> List[str]:
    """return a list of the player choices

    Args:
        move1 (str): The first player's move
        move2 (str): The second player's move
        computer (bool, optional): If the second player is the computer. Defaults to False.

    Returns:
        List[str]: A list of the player choices in the format "playerName chose: choice"
    """
    # "Player1 chose: rock"
    if computer:
        return [(f"{player1Name} chose: {printMove(move1)}"),
                (f"{computerName} chose: {printMove(move2)}")]
    else:
        return [(f"{player1Name} chose: {printMove(move1)}"),
                (f"{player2Name} chose: {printMove(move2)}")]


def printWinner(gameState: int, computer=False) -> None:
    """Print the winner of the game with the win message

    Args:
        gameState (int): The winner of the game in the standard representation
        computer (bool, optional): If the second player is the computer. Defaults to False.

    Raises:
        ValueError: _description_
    """
    # print the winner message
    print(winMessage, end=': ')
    # print the winner name
    match gameState:
        case 0:
            # draw
            print("No one!")
        case 1:
            # player 1
            print(player1Name)
        case 2:
            # computer
            if computer:
                print(computerName)
            # player 2
            else:
                print(player2Name)
        case _:
            # invalid game state
            raise ValueError("Invalid game")


def pickMove(name: str) -> str:
    """Get the player's move after prompting them with the prompt message

    Args:
        name (str): The name of the player. Preferably one of the global variables

    Returns:
        str: The player's move, in lowercase
    """

    # "Player1, Please make a move (rock, paper, scissors): "
    return str(input(f'{name}, {movePrompt}: ')).lower()


def sgGame():
    # run a singleplayer game
    cls(sgPlayerMessage)

    # get the computer's move
    computer = choice(list(winning_moves.keys()))

    # get the player's move
    player = pickMove(player1Name)
    # check if the move is valid
    printMove(player)

    # get the outcome of the game
    game = rps(player, computer)

    # print the player choices
    cls(sgPlayerMessage)
    for player in printPlayers(player, computer, True):
        print(player)

    # print the winner
    printWinner(game, True)

    # wait for user confirmation to continue
    input(f"{confirmationPrompt}: ")


def multiGame():
    # run a multiplayer game

    # get the move of the first player
    cls(mlPlayerMessage)
    player1 = pickMove(player1Name)
    # check if the move is valid
    printMove(player1)

    # get the move of the second player
    cls(mlPlayerMessage)
    player2 = pickMove(player2Name)
    # check if the move is valid
    printMove(player2)

    # get the outcome of the game
    game = rps(player1, player2)

    # print player choices
    cls(mlPlayerMessage)
    for player in printPlayers(player1, player2):
        print(player)

    # print the winner
    printWinner(game)

    # wait for user confirmation to continue
    input(f"{confirmationPrompt}: ")


if __name__ == "__main__":
    main()
