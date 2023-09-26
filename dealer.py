from utils import get_random_card, create_player_hand, score_hand, open_modal

class Dealer:
    def __init__(self, deck, score_label, hand, frame, card, player_cards, root):
        self.hand = hand
        self.deck = deck
        self.card = card
        self.score_label = score_label
        self.frame = frame
        self.player_cards = player_cards
        self.root = root

    def add_card_to_dealer(self):
        dealer_cards = self.card
        card = get_random_card(dealer_cards, deck=self.deck)
        dealer_score = score_hand(dealer_cards)
        self.score_label.set(dealer_score)
        self.hand.append(create_player_hand(card, self.frame, dealer_cards))
    def handle_player(self):
        root = self.root
        dealer_score = score_hand(self.card)
        while 0 < dealer_score < 17:
            card = get_random_card(card=self.card, deck=self.deck)
            dealer_score = score_hand(self.card)
            self.score_label.set(dealer_score)
            self.hand.append(create_player_hand(card, self.frame, self.card))
        player_score = score_hand(self.player_cards)
        if player_score > 21:
            open_modal("Dealer wins!", root=root)
        elif dealer_score > 21 or dealer_score < player_score:
            open_modal("player wins!", root=root)
        elif dealer_score > player_score:
            open_modal("Dealer Wins!", root=root)
        else:
            open_modal("Draw!", root=root)