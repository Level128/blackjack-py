import unittest
from game import *

MAX_CARDS_PER_DECK = 52


class TestDeckOfCards(unittest.TestCase):
    def setUp(self) -> None:
        """
        Setup used for the following tests
        """
        random.seed(42)
        self.number_of_decks = 1
        self.Deck = Deck(number_of_decks=self.number_of_decks)
        return super().setUp()

    def test_new_deck(self):
        """
        Test to make sure new deck is of the correct size
        """
        self.assertEqual(len(self.Deck.cards),
                         (self.number_of_decks * MAX_CARDS_PER_DECK))

    def test_draw_card(self):
        """
        Pops last card added to pile, which would be a king of spades
        """
        card = self.Deck.draw_card()
        self.assertEqual(card.suit_icon, "♠")
        self.assertEqual(card.value, 10)
        self.assertEqual(card.card_rank_name, "king")
        self.assertEqual(card.card_rank_label, "K")

    def test_print_card_string(self):
        """
        Pops last card added to pile, which would be a king of spades, and tests the string method
        """
        card = self.Deck.draw_card()
        self.assertEqual(card.suit_icon, "♠")
        self.assertEqual(card.value, 10)
        self.assertEqual(card.card_rank_name, "king")
        self.assertEqual(card.card_rank_label, "K")
        self.assertEqual(str(card), "♠K")

    def test_draw_till_empty(self):
        """
        Draws all cards from deck
        """
        while len(self.Deck.cards) > 0:
            self.Deck.draw_card()
        self.assertEqual(len(self.Deck.cards), 0)
        self.Deck.draw_card()
        self.assertEqual(len(self.Deck.cards),
                         (self.number_of_decks * MAX_CARDS_PER_DECK) - 1)

    def test_exhaustive_draw(self):
        """
        Tests a stress test on the Deck
        """
        for i in range(10_000):
            self.test_draw_till_empty()


class TestPlayer(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(42)
        self.number_of_decks = 1
        self.Deck = Deck(number_of_decks=self.number_of_decks)
        self.test_player = Player("test_player")
        return super().setUp()
    
    def test_print_hand(self):
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.hit(self.Deck)
        self.test_player.print_hand()


if __name__ == '__main__':
    unittest.main()
