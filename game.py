import random
from xmlrpc.client import Boolean


class Card:
    rank_values = {
        'ace': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'jack': 10,
        'queen': 10,
        'king': 10
    }
    rank_labels = {
        'ace': "A",
        'two': "2",
        'three': "3",
        'four': "4",
        'five': "5",
        'six': "6",
        'seven': "7",
        'eight': "8",
        'nine': "9",
        'ten': "10",
        'jack': "J",
        'queen': "Q",
        'king': "K"
    }

    suit_icons = {'clubs': '♣', 'diamonds': '♦', 'hearts': '♥', 'spades': '♠'}

    def __init__(self, suit, card_rank_name):
        self.suit = suit
        self.suit_icon = self.suit_icons.get(self.suit)
        self.card_rank_name = card_rank_name
        self.value = self.rank_values.get(card_rank_name)
        self.card_rank_label = self.rank_labels.get(card_rank_name)

    def __str__(self) -> str:
        return self.suit_icon + self.card_rank_label

    def print_card(self) -> None:
        # print("-" * 9)
        # print(f"| {self.suit_icon}{' ' * 5}|")
        # for i in range(3):
        #     print("|         |")
        # print(
        #     f"|{' ' * 3}{self.card_rank_label}{' ' * (4 - len(self.card_rank_label))}|")
        # for i in range(3):
        #     print("|         |")
        # print(f"|{' ' * 5}{self.suit_icon} |")
        # print("-" * 9)
        print(self.build_card_to_print())

    def build_card_to_print(self) -> str:
        card_string = ""
        card_string += ("-" * 9) + "\n"
        card_string += (f"| {self.suit_icon}{' ' * 5}|") + "\n"
        for i in range(3):
            card_string += ("|       |") + "\n"
        card_string += (
            f"|{' ' * 3}{self.card_rank_label}{' ' * (4 - len(self.card_rank_label))}|") + "\n"
        for i in range(3):
            card_string += ("|       |") + "\n"
        card_string += (f"|{' ' * 5}{self.suit_icon} |") + "\n"
        card_string += ("-" * 9) + "\n"
        return card_string


class Deck:
    suits = ('clubs', 'diamonds', 'hearts', 'spades')
    card_rank_names = ('ace', 'two', 'three', 'four', 'five', 'six',
                       'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king')

    def __init__(self, number_of_decks=1) -> None:
        self.cards = []
        self.number_of_decks = number_of_decks
        self.populate_cards()

    def populate_cards(self) -> None:
        """
        Used once deck of cards are empty. Reinitiates the deck with all new cards in order
        """
        for decks in range(self.number_of_decks):
            for suit in self.suits:
                for value in self.card_rank_names:
                    self.cards.append(Card(suit, value))

    def shuffle(self) -> None:
        return random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            self.populate_cards()
            self.shuffle()
        return self.cards.pop()


class Player:
    def __init__(self, name) -> None:
        self.hand = []
        self.total = 0
        self.name = name

    def get_hand_total(self) -> int:
        hand_total = 0
        for card in self.hand:
            hand_total += card.value
        return hand_total

    def check_for_blackjack(self) -> bool:
        if self.get_hand_total == 21:
            return True
        return False

    def check_for_bust(self) -> bool:
        if self.get_hand_total() > 21:
            return True
        return False

    def hit(self, deck: Deck):
        self.hand.append(deck.draw_card())

    def print_name(self):
        print(self.name)

    def print_hand(self):
        card_strings = []
        output = "\n"
        for card in self.hand:
            card_strings.append(card.build_card_to_print().splitlines())
        if len(card_strings) == 0:
            return
        for line_number in range(len(card_strings[0])):
            for card in card_strings:
                output += card[line_number] + " "
            output += "\n"
        print(output)
        return output


class Dealer(Player):
    def __init__(self) -> None:
        super().__init__("Dealer")


class User(Player):
    pass


class Table:
    def __init__(self) -> None:
        self.dealer = Dealer()
        self.players = {}

    def add_player(self, new_player: User):
        self.players[len(self.players) + 1] = new_player


def main():
    # player1 = User("Player1")
    # print(player1.get_hand_total())
    # dealer = Dealer()
    # dealer.print_name()
    # player1.print_name()
    Card("hearts", "ace").print_card()


if __name__ == '__main__':
    main()
