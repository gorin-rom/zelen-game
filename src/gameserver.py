import inspect
from random import randint
from src.card import Card
from src.deck import Deck
from src.hand import Hand
from src.gamestate import GameState
from src.player import Player
import enum
from src.price import VegBox


class GamePhase(enum.StrEnum):
    CHOOSE_CARD = "Choose card"
    NEXT_PLAYER = "Switch current player"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"


class GameServer:
    def __init__(self, player_types, gamestate):
        self.gamestate = gamestate
        self.player_types = player_types


    def new_game(self):
        player_count = self.request_player_count()
        player_types = {}
        for p in range(player_count):
            name, kind = self.request_player_count()
            player = Player(name, Hand())
            player_types[player] = kind

        deck = Deck(cards=[Card(veg) for veg in Card.VEGETABLES])
        self.gamestate = GameState(list(player_types.keys()), deck)

    def run(self):
        current_phase = GamePhase.CHOOSE_CARD
        while current_phase != GamePhase.GAME_END:
            phases = {
                GamePhase.CHOOSE_CARD: self.choose_card_phase,
                GamePhase.NEXT_PLAYER: self.next_player_phase,
                GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()

    def choose_card_phase(self) -> GamePhase:
        pass

    def next_player_phase(self) -> GamePhase:
        if GameState.round == 6:
            return GamePhase.DECLARE_WINNER
        self.gamestate.next_player()
        print(f"=== {self.gamestate.current_player()}'s turn")
        return GamePhase.CHOOSE_CARD

    def declare_winner_phase(self) -> GamePhase:
        max_score = 0
        winner = None
        for player in self.gamestate.players:
            if player.hand.score > max_score:
                max_score = player.hand.score
                winner = player
        print(f"{winner.name} is the winner!")
        return GamePhase.GAME_END

    @staticmethod
    def request_player_count() -> int:
        while True:
            try:
                count = int(input("Введите количество игроков: "))
                if 2 <= count <= 6:
                    return count
            except ValueError:
                pass
            print("Пожалуйста, введите корректное число.")


def __main__():
    server = GameServer({}, None)
    server.new_game()
    server.run()


if __name__ == "__main__":
    __main__()