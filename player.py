from utils import get_random_card, create_player_hand, score_hand, open_modal
class Player:
    def __init__(self, deck, score_label, hand, frame, card,root):
        self.hand = hand
        self.deck = deck
        self.card = card
        self.score_label = score_label
        self.frame = frame
        self.root = root

    def handle_player(self):
        deck = self.deck
        player_cards = self.card
        if score_hand(player_cards) < 21:
            card = get_random_card(player_cards, deck=deck)
            score = score_hand(player_cards)
            self.score_label.set(score)
            self.hand.append(create_player_hand(card, self.frame, player_cards))
        if score_hand(player_cards) > 21:
            open_modal("Dealer Wins!",self.root)
    