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
            player_types[player] = kind.lower()
        return player_types

    def new_game(self, player_types: dict):
        deck = Deck(cards=None)
        deck.shuffle()
        price = VegBox()
        self.gamestate = GameState(list(player_types.keys()), deck, price, cards=[])

    def run(self):
        current_phase = GamePhase.BEGIN_ROUND
        while current_phase != GamePhase.GAME_END:
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
        print(f"******* {self.gamestate.iround}-й раунд *******")
        print(f"Цена: {self.gamestate.price.save()}")
        return GamePhase.CHOOSE_CARD

    def choose_card_phase(self) -> GamePhase:
        current_player = self.gamestate.current_player()
        print(f"=== Ход игрока {current_player.name} ===")
        print(f"Карты: {self.gamestate.cards}")
        while True:
            if self.player_types[current_player] == "human":
                try:
                    num = int(input(f"{current_player.name}, какую карту тянем?: "))
                    if GameState.MIN_PLAYABLE_CARD <= num <= len(self.gamestate.cards):
                        choose_card = self.gamestate.cards[num - 1]
                        self.gamestate.cards.remove(choose_card)
                        current_player.hand.cards.append(choose_card)
                        print(f"Игрок {current_player.name} выбрал {choose_card}")
                        break
                    else:
                        print("Некорректный ввод. Пожалуйста, выберите номер карты из доступных.")
                except ValueError:
                    print("Пожалуйста, введите корректное число.")

            elif self.player_types[current_player] == "bot":
                choose_card = self.gamestate.cards[randint(0, len(self.gamestate.cards) - 1)]
                self.gamestate.cards.remove(choose_card)
                current_player.hand.cards.append(choose_card)
                print(f"Игрок {current_player.name} (бот) выбрал {choose_card}")
                break
        return GamePhase.NEXT_PLAYER

    def next_player_phase(self) -> GamePhase:
        if len(self.gamestate.cards) == GameState.MIN_PLAYABLE_CARD:
            print(f"На столе осталась карта {self.gamestate.cards[0]}")
            return GamePhase.END_ROUND
        else:
            self.gamestate.next_player()
            return GamePhase.CHOOSE_CARD

    def end_round_phase(self) -> GamePhase:
        print(f"--- {self.gamestate.iround}-й раунд завершён---\n")

        remaining_card = self.gamestate.cards[0]
        self.gamestate.price.add(remaining_card)

        self.gamestate.iround += 1
        self.gamestate.cards.clear()  # Очистка стола от карт после раунда

        # Если раунд достиг максимального значения, конец игры
        if self.gamestate.iround > GameState.MAX_ROUND:
            print(f'*** Итоговая цена ***\n {self.gamestate.price.save()}')
            return GamePhase.DECLARE_WINNER

        return GamePhase.BEGIN_ROUND  # Переход к следующему раунду (по умолчанию)

    def declare_winner_phase(self) -> GamePhase:
        max_score = 0
        winner = None
        player_score = {}
        for player in self.gamestate.players:
            current_score = sum(card.score(self.gamestate.price) for card in player.hand.cards)
            player_score[player.name] = current_score
            if current_score > max_score:
                max_score = current_score
                winner = player
        for name, score in player_score.items():
            print(f"{name}: {score} очков")
        if winner:
            print(f"{winner.name} - ПОБЕДИТЕЛЬ: {max_score} очков!")

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

