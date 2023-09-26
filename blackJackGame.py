from player import Player
from dealer import Dealer
import tkinter as tk

class BlackjackGame:
    def __init__(self, root,):
        self.root = root
        self.player_score_label = tk.IntVar()
        self.dealer_score_label = tk.IntVar()
        self.deck = []
        self.player_cards = []
        self.dealer_cards = []
        self.player_hand = []
        self.dealer_hand = []
        self.dealer_frame = tk.Frame(root,width=500,)
        self.player_frame = tk.Frame(root, width=500,)
        self.player = Player(deck=self.deck, score_label=self.player_score_label, hand=self.player_hand, frame=self.player_frame, card=self.player_cards, root=root)
        self.dealer = Dealer(deck=self.deck, score_label=self.dealer_score_label, hand=self.dealer_hand, frame=self.dealer_frame, card=self.dealer_cards, player_cards=self.player_cards, root=root)
        
        
        self.load_images(self.deck)

    def start(self):
        self.create_game_components()

    def create_game_components(self):
        root =  self.root
        root.title("Blackjack")
        root.geometry('600x400')
        main_heading = tk.Label(root, text="Player & Dealer Cards")
        main_heading.grid(row=0, column=0, sticky='we')

        player_cards_label = tk.Label(root, text="Player Cards")
        player_cards_label.grid(row=1, column=0,  sticky='w')
        self.player_frame.grid(row=2, column=0, sticky='w')
        dealer_cards_label = tk.Label(root, text="Dealer Cards")
        dealer_cards_label.grid(row=3, column=0,  sticky='w')
        self.dealer_frame.grid(row=4, column=0, sticky='w')


        controlls_frame = tk.Frame(root,width=500)
        controlls_frame.grid(row=5, column=0,  ) 
       
        player_dealer_score_frame = tk.Frame(root, width=500)
        player_dealer_score_frame.grid(row=6, column=0, )


        tk.Label(player_dealer_score_frame, text='player score').grid(row=0,column=0, )
        tk.Label(player_dealer_score_frame, textvariable=self.player_score_label).grid(row=0,column=1, )

       
       
        tk.Label(player_dealer_score_frame, text='dealer score').grid(row=1,column=0, )
        tk.Label(player_dealer_score_frame, textvariable=self.dealer_score_label).grid(row=1,column=1,)
        
        tk.Button(controlls_frame, text="Dealer", command=lambda: click_user(action="Dealer")).pack(side='left')
        tk.Button(controlls_frame, text="Player", command=lambda: click_user(action="Player")).pack(side='left')
        
        
        
        self.player.handle_player()
        self.dealer.add_card_to_dealer()
        # self.player.handle_player()
        def click_user(action):
            if action == 'Dealer':
               self.dealer.handle_player()
                
            elif action == 'Player':
                self.player.handle_player()

    def new_game(self):
        self.player_frame.destroy()
        self.dealer_frame.destroy()

        self.player_hand.clear()
        self.dealer_hand.clear()
       


    def load_images(self, card_images):
        # Load card images
        suits = ["heart", "club", "diamond", "spade"]
        picture_cards = ["jack", "queen", "king"]
        extension = "png"

        # for each suit, retrieve the image for the cards from cards directory
        for suit in suits:
            # non picture cards
            for card in range(1, 11):
                name = f"cards/{str(card)}_{suit}.{extension}"
                image = tk.PhotoImage(file=name)
                card_images.append((card, image))

            # picture cards
            for card in picture_cards:
                name = f"cards/{str(card)}_{suit}.{extension}"
                image = tk.PhotoImage(file=name)
                card_images.append((10, image))
   

   
    # Define other game logic methods like handling player, dealer, scoring, etc.

