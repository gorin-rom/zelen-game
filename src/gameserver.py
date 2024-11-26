import inspect
import sys
from random import randint
from src.card import Card
from src.deck import Deck
from src.hand import Hand
from src.gamestate import GameState
from src.player import Player
import enum
from src.price import VegBox


class GamePhase(enum.StrEnum):
    BEGIN_ROUND = "Deal cards"
    CHOOSE_CARD = "Choose card"
    NEXT_PLAYER = "Switch current player"
    END_ROUND = "Price change"
    DECLARE_WINNER = "Declare a winner"
    GAME_END = "Game ended"


class GameServer:
    def __init__(self, player_types, gamestate):
        self.gamestate = gamestate
        self.player_types = player_types

    @classmethod
    def get_players(cls):
        player_count = cls.request_player_count()

        player_types = {}
        for _ in range(player_count):
            name, kind = cls.request_player()
            player = Player(name, Hand())
            player_types[player] = kind
        return player_types

    def new_game(self, player_types: dict):
        deck = Deck(cards=None)
        deck = deck.shuffle()
        price = VegBox()
        self.gamestate = GameState(list(player_types.keys()), deck, price, cards=[])

    def run(self):
        current_phase = GamePhase.BEGIN_ROUND
        while current_phase != GamePhase.DECLARE_WINNER:
            phases = {
                GamePhase.BEGIN_ROUND: self.begin_round_phase,
                GamePhase.CHOOSE_CARD: self.choose_card_phase,
                GamePhase.NEXT_PLAYER: self.next_player_phase,
                GamePhase.END_ROUND: self.end_round_phase,
                GamePhase.DECLARE_WINNER: self.declare_winner_phase,
            }
            current_phase = phases[current_phase]()

    def begin_round_phase(self) -> GamePhase:
        self.gamestate.deal_cards()
        print(self.gamestate.cards)

        return GamePhase.CHOOSE_CARD

    def choose_card_phase(self) -> GamePhase:
        pass

    def next_player_phase(self) -> GamePhase:
        if GameState.iround == GameState.MAX_ROUND:
            return GamePhase.DECLARE_WINNER
        self.gamestate.next_player()
        print(f"=== {self.gamestate.current_player()}'s turn")
        return GamePhase.CHOOSE_CARD

    def end_round_phase(self) -> GamePhase:
        pass

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
                print(f'Ввели {count}')
                if GameState.MIN_PLAYERS <= count <= GameState.MAX_PLAYERS:
                    return count
            except ValueError:
                pass
            print("Пожалуйста, введите число от 2 до 6")

    @staticmethod
    def request_player() -> (str, str):
        """Возвращает имя и тип игрока"""

        while True:
            name = input("Введите имя игрока ")
            if name.isalpha():
                break
            print("Имя должно быть одним словом, только алфавитные символы")

        while True:
            kind = input("Какой тип игрока? (введите 'human' или 'bot') ")
            if kind.lower() in ['human', 'bot']:  # Проверка на корректный ввод типа игрока
                break
            print("Допустимые типы игроков: 'human' или 'bot'")

        return name, kind
def __main__():
    player_types = GameServer.get_players()
    server = GameServer(player_types, gamestate=None)
    server.new_game(player_types)
    server.run()


if __name__ == "__main__":
    __main__()

