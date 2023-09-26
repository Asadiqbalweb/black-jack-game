import tkinter as tk
import random
def create_player_hand(image, frame, card):
            image_label = tk.Label(frame,image=image[1], height=150, anchor='w')
            image_label.image = image[1] 
            col = len(card)
            return image_label.grid(row=0, column=col, )

def get_random_card(card, deck):
    player_card = random.choice(deck)
    deck.remove(player_card)
    card.append(player_card)
    return player_card

def score_hand(hand):
        score = 0
        ace = False
        for next_card in hand:
            card_value = next_card[0]
            if card_value == 1 and not ace:
                ace = True
                card_value = 11
            score += card_value
            if score > 21 and ace:
                score -= 10
                ace = False
        return score

def open_modal(result, root):
    modal_window = tk.Toplevel(root)
    modal_window.title("Modal Dialog")
    
    label = tk.Label(modal_window, text=result)
    label.pack(padx=20, pady=20)
    
    close_button = tk.Button(modal_window, text="Close", command=modal_window.destroy)
    close_button.pack(side='left')
    close_game = tk.Button(modal_window, text="Quit Game", command=root.quit)
    close_game.pack(side='right')

